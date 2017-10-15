numero=int(raw_input('Ingrese numero: '))

divisor = 0
c = 0
while c < numero:
    divisor = divisor +1
    division = numero % divisor

    if division == 0:
        print divisor,
    c = c+1
