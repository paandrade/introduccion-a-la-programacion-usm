dividendo=int(raw_input('Dividendo: '))
divisor=int(raw_input('Divisor: '))

cociente=dividendo//divisor
resto=dividendo%divisor

if resto==0:
    print 'la division es exacta'
    print 'cociente: ',cociente
    print 'resto: ', resto

if resto!=0:
    print 'la division no es exacta'
    print 'cociente: ',cociente
    print 'reso: ', resto
