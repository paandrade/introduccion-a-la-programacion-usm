print ' ingrese lados a, b, c del triangulo'

a=float(raw_input('Ingrese a: '))
b=float(raw_input('Ingrese b: '))
c=float(raw_input('Ingrese c: '))

suma_ab = a + b
suma_ac = a + c
suma_bc = b + c

if a > suma_bc or b > suma_ac or c > suma_ab:
    print 'No es un triangulo valido'

else:
    if a == b == c:
        print 'El triangulo es equilatero'
    elif a == b or a == c or b == c :
        print 'El triangulo es isoceles'
    elif a != b and a != c and b != c:
        print 'El triangulo es escaleno'
