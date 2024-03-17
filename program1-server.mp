SEQ
result = 0
c_channel calc("localhost","localhost")
operation = 'null'
valor1 = 0
valor2 = 0

Output("Aguardando conexões\n\n")
calc.receive(operation, valor1, valor2, result)
Output("Conexão estabelecida\nOperação: ", valor1,operation,valor2,"\n\n")

if (operation == '-'){
    result = valor1 - valor2
}
if (operation == '+'){
    result = valor1 + valor2
}
if (operation == '*'){
    result = valor1 * valor2
}
if (operation == '/') {
    result = valor1 / valor2
}

Output("Resultado: ", result, "\n\n")
Output("Enviando resultado\n")
calc.send(result)
