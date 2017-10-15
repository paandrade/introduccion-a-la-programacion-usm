num1=int(raw_input('Ingrese num: '))
num2=int(raw_input('Ingrese num: '))


if num1 < num2:
    dif = num2 - num1
    c = 1
    numero_movil = 1+num1
    suma = 0
    while c < dif : 
        suma = suma + numero_movil
        numero_movil= numero_movil + 1

        c=c+1
    print suma

if num2 < num1:
    dif = num1 - num2
    c = 1
    numero_movil = 1+num2
    suma = 0
    while c < dif : 
        suma = suma + numero_movil
        numero_movil= numero_movil + 1

        c=c+1
    print suma
