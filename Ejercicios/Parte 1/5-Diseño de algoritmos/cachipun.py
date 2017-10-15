marcador_a=0
marcador_b=0

while marcador_a != 3 and marcador_b != 3:
    a = raw_input('A: ')
    b = raw_input('B: ')

    if a == b :
        marcador_a += 0
        marcador_b += 0
        print marcador_a,'-',marcador_b
        
    elif a == 'tijera' and b == 'piedra':
        marcador_a += 0
        marcador_b += 1
        print marcador_a,'-',marcador_b
        
    elif a == 'tijera' and b == 'papel':
        marcador_a += 1
        marcador_b += 0
        print marcador_a,'-',marcador_b

    elif a == 'piedra' and b == 'papel':
        marcador_a += 0
        marcador_b += 1
        print marcador_a,'-',marcador_b

    elif a == 'piedra' and b == 'tijera':
        marcador_a += 1
        marcador_b += 0
        print marcador_a,'-',marcador_b

    elif a == 'papel' and b == 'piedra':
        marcador_a += 1
        marcador_b += 0
        print marcador_a,'-',marcador_b
        
    elif a == 'papel' and b == 'tijera':
        marcador_a += 0
        marcador_b += 1
        print marcador_a,'-',marcador_b

if marcador_a == 3:
    print 'A es el ganador'
else:
    print 'B es el ganador'
    
