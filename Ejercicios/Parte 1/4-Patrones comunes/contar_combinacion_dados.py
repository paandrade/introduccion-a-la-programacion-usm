puntaje = int(raw_input('Ingrese puntaje: '))

dado1 = 1
dado2 = 1
comb = 0

if 2 <= puntaje <= 12:
    while dado1 <=6:
        dado2=1
        while dado2 <=6:
            suma = dado1 + dado2
            if suma == puntaje:
                comb = comb + 1
            dado2 = dado2 + 1
        dado1 = dado1 + 1

    print 'Hay ',comb,' combinaciones para obtener ',puntaje

else:
    print 'Hay ',comb,' combinaciones para obtener ',puntaje
