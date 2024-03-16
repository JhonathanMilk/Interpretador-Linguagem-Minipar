import socket
import threading

has_error = False
symbol_table = {}
channels = {}

# Funções de execução
def execute_stmt(stmt):     
    #time.sleep(1)
    #print("stmt: ", stmt[0])
    if stmt[0] == 'SEQ':
        for s in stmt[1]:
            #print(s)
            #print("SEQ")
            execute_stmt(s)
    elif stmt[0] == 'PAR':
        threads = []
        for s in stmt[1]:
            #print(s)
            #print("PAR")
            thread = threading.Thread(target=execute_stmt, args=(s,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
            
    elif stmt[0] == 'IF':
        if execute_bool(stmt[1]):
            for s in stmt[2]:
                execute_stmt(s)
    elif stmt[0] == 'WHILE':
        while execute_bool(stmt[1]):
            for s in stmt[2]:
                execute_stmt(s)
    elif stmt[0] == 'INPUT':
        var_name = stmt[1]
        var_value = input()
        symbol_table[var_name] = var_value

    elif stmt[0] == 'OUTPUT':
        #print("aqui: ", stmt[1])
        if isinstance(stmt[1], tuple):
            for v in stmt [1]:
                execute_output(v)
        else:
            execute_output(stmt[1])
    
    elif stmt[0] == '=':
        var_name = stmt[1]
        value = stmt[2]

        #print("var_name: ", var_name)
        #print("value: ", value)
        
        if (value == "INPUT"):        #Se for um input tem que chamar o Elif 'INPUT' em execute_stmt para pegar o input
            value = execute_stmt((value, var_name))     
            # print("value2: ", value)
        
        #elif isinstance(value, tuple) and value[0] in channels:         #para atribuições de channel: ex: y = calc.receive
        #    value = execute_stmt(value)

        #elif isinstance(value, tuple):  # Se for uma expressão
        #    value = evaluate_expr(value)
        #    symbol_table[var_name] = value
        else:
            value = evaluate_expr(value)
            symbol_table[var_name] = value

            
    elif stmt[0] == "C_CHANNEL":
        channels[stmt[1]] = (stmt[2], stmt[3])

    elif not isinstance(stmt[0], tuple) and stmt[0] in channels:
        #print(symbol_table)
        #print(stmt)
        if stmt[1] == 'SEND':
            channel_name = stmt[0]
            channel = channels.get(channel_name)
            if channel:
                if (len(stmt) == 6):
                    _, _, operation, value1, value2, result = stmt
                    send_data(channel[1], 9999, f"{symbol_table[operation]},{symbol_table[value1]},{symbol_table[value2]},{result}")
                elif (len(stmt) == 3):
                    send_data(channel[1], 9998, f"{symbol_table[stmt[2]]}")


        elif stmt[1] == "RECEIVE":
            channel_name = stmt[0]
            channel = channels.get(channel_name)
            if channel:
#                print("stringRec: ", stringRec)
                if (len(stmt) == 6):
                    stringRec = receive_data(channel[1], 9999)
                    operation, value1, value2, result = stringRec.split(",")
                    symbol_table[stmt[2]] = operation
                    symbol_table[stmt[3]] = int(value1)
                    symbol_table[stmt[4]] = int(value2)
                    symbol_table[stmt[5]] = result
                elif (len(stmt) == 3):
                    stringRec = receive_data(channel[1], 9998)
                    symbol_table[stmt[2]] = stringRec
        
    elif isinstance(stmt, tuple):
        for s in stmt:
            execute_stmt(s)

def execute_output(v):
    #print("v: ", v)
    var_name = v
    var_value = symbol_table.get(var_name, None)
    if var_value is not None:
        formatted_output = var_value
        print(formatted_output, end='')
    else:
        #print(f"Variável '{var_name}' não encontrada na tabela de símbolos")
        formatted_output = var_name.replace("\\n", "\n")
        print(formatted_output, end='')

def execute_bool(expr):
    if isinstance(expr, tuple):

        op, left, right = expr

        if left in symbol_table:
            left = symbol_table.get(left, 0)  # Obter o valor da variável ou 0 se não existir
        if right in symbol_table:
            right = symbol_table.get(right, 0)  # Obter o valor da variável ou 0 se não existir
        
        #print(left, op, right)
            
        if op == '<':
            return evaluate_expr(left) < evaluate_expr(right)
        elif op == '>':
            return evaluate_expr(left) > evaluate_expr(right)
        elif op == '<=':
            return evaluate_expr(left) <= evaluate_expr(right)
        elif op == '>=':
            return evaluate_expr(left) >= evaluate_expr(right)
        elif op == '==':
            return evaluate_expr(left) == evaluate_expr(right)
        elif op == '!=':
            return evaluate_expr(left) != evaluate_expr(right)
    return False

def evaluate_expr(expr):
    if isinstance(expr, int) or expr in {'-', '+', '*', '/'}:
        return expr
    elif isinstance(expr, tuple):
        op, left, right = expr
        if op == '+':
            return evaluate_expr(left) + evaluate_expr(right)
        elif op == '-':
            return evaluate_expr(left) - evaluate_expr(right)
        elif op == '*':
            return evaluate_expr(left) * evaluate_expr(right)
        elif op == '/':
            return evaluate_expr(left) / evaluate_expr(right)
        elif any(op == x for x in ['<', '>', '<=', '>=', '==', '!=']):
            return execute_bool(expr)
    elif isinstance(expr, str):
        return symbol_table.get(expr, expr)  # Retorna o valor da variável na tabela de simbolos, se não tiver retorna a propria string


def send_data(host, port, data):
    #print(f"host: {host} \nport: {port} \ndata: {data}")
    # Cria um socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conecta ao host e porta especificados
        sock.connect((host, port))
        # Envia os dados
        sock.sendall(data.encode())
    finally:
        # Fecha o socket
        sock.close()
        #print("conexão cliente fechada")


def receive_data(host, port):
    #print(f"host: {host} port: {port}")
    # Cria um socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Associa o socket ao host e à porta especificados
        server_socket.bind((host, port))
        # Escuta por conexões
        server_socket.listen(5)
        #print("Aguardando conexão...")
        
        while True:
            # Aceita a conexão
            client_socket, address = server_socket.accept()
            #print(f"Conexão estabelecida com {address}")
            
            # Recebe os dados
            data = client_socket.recv(1024)
            if not data:
                break
            #print(f"Dados recebidos: {data.decode()}")
            
            # Retorna a string recebida
            return data.decode()
            # Fecha o socket do cliente
            client_socket.close()
    finally:
        # Fecha o socket do servidor
        server_socket.close()