numero = int(raw_input('n: '))


while numero > 1:
    print numero,
    if numero%2 == 0:
        numero = numero / 2
    else:
        numero = (numero*3) + 1
        
print 1,
