from random import randrange


rango=int(raw_input('Ingrese rango: '))
print 'Adivine el numero'
n = randrange(rango)
intentos = 1
intento = 0

while intento != n :
    intento=int(raw_input('Intento: '))
    if intento < n :
        print 'es mayor que',intento
        intentos += 1
    elif intento > n :
        print 'es menor que',intento
        intentos += 1
print 'correcto. Adivinaste en',intentos,'intentos.'

raw_input()
        
