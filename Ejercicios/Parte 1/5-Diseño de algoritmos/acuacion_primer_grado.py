print 'escuacion aX + b = 0'
a = float(raw_input('Ingrese a: '))
b = float(raw_input('Ingrese b: '))

if a == 0 and b != 0:
    print 'sin solucion'

elif a != 0:
    sol = (-b)/a
    print 'solucion unica: ',sol

else:
    print 'no hay solucion unica'
