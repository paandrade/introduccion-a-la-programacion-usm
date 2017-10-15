cant_numeros=int(raw_input('Cuantos numeros: '))

suma = 0
i = 0

while i < cant_numeros:
    numero = float(raw_input('n = '))
    suma = suma + (1/numero)
    i = i + 1

H = cant_numeros/suma

print 'H = ', H
