print 'Ingrese varios valores, termine con cero:'
positivos= 0
negativos= 0
inicio = True

while inicio:
    numero = int(raw_input())
    if numero > 0:
        positivos = positivos + 1
    elif numero < 0:
        negativos = negativos + 1
    else:
        inicio = False

print 'Positivos: ','*'*positivos
print 'Negativos: ','*'*negativos
        
