SEQ
result = 0
c_channel calc("localhost","localhost")
operation = 'null'
valor1 = 0
valor2 = 0
calc.receive(operation, valor1, valor2, result)
if (operation == '-'){
    z = valor1 - valor2
}
if (operation == '+'){
    z = valor1 + valor2
}
if (operation == '*'){
    z = valor1 * valor2
}
if (operation == '/') {
    z = valor1 / valor2
}
Output(z, "\n")
calc.send(z)
