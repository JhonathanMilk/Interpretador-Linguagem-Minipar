SEQ
Output("CALCULADORA\n\n")
Output("Operadores: + - * /\n\n")

Output("Digite o primeiro numero:\n")
valor1 = Input()
            
Output("Digite o segundo numero\n")
valor2 = Input()

Output("Digite a operacao entre os números\n")
operation = Input()

result = 0
c_channel calc("localhost","localhost")

calc.send(operation, valor1, valor2, result)
calc.receive(result)

Output(result)