SEQ
# Inicializando variaveis para calc do fatorial
numero = 9
fatorial = 1
i = 1
k = "ola carinha"

Output(k)

# Inicializando variaveis para serie de fibonnaci
n = 10  # Número de termos da série Fibonacci
a = 0   #primeiro termo
b = 1   #segundo termo
j = 2   #count inicia em 2

PAR
while (i <= numero){
    fatorial = fatorial * i
    i = i+1
}

Output("Série de Fibonacci:\n\n")    
Output(a, " ")
Output(b, " ")

while (j < n ){
    c = a + b
    Output(c)
    a = b
    b = c
    j = j+1
}
Output("\n")
SEQ
Output(fatorial, "\n")