#Ingrese n notas. por cada nota veifique si es mayor que 80
#menor igual que 80 y mayo igual que 55, y menor que 55
#El programa felicita, dice BKN, o manda a estudiar, respectivamente

n=int(raw_input('ingrese n: '))

c=0 #contador
while c < n:
    nota=int(raw_input('ingrese nota: '))
    if nota > 80:
        print 'Felicitaciones'
    elif 55 <= nota <=80:
        print 'BKN'
    else:
        print 'estudia mas'
    c=c+1
