print 'ingrese sus notas'

c=0
suma=0

while c < 5:
    nota=float(raw_input('Ingrese nota: '))
    c = c + 1
    suma= suma + nota

promedio= suma/c

print 'Promedio es ',promedio
