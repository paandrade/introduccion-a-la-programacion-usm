n = int(raw_input('Ingrese n: '))
i=0
mayor= -float('inf')

while i < n :
    numero = int(raw_input('ingrese numero: '))
    if numero > mayor:
        mayor = numero
        i = i + 1
    else:
        i = i + 1

print 'el mayor es ',mayor
