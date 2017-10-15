num=float(raw_input('Ingrese un numero: '))

if num>0:
    num=num*1000
    num=num%1000
    num=num/1000
    print 'la parte decimal es: ',num

if num<0:
    num=num*(-1)
    num=num*1000
    num=num%1000
    num=num/1000
    print 'la parte decimal es: ', num


