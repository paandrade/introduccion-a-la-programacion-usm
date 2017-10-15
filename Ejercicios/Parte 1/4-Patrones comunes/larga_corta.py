cant_palabras=int(raw_input('Cantidad de palabras: '))

i=0
mayor = -float('inf')
menor = float('inf')
larga = ''
corta = ''

while i < cant_palabras :
    palabra = raw_input('Palabra: ')

    if len(palabra) > mayor:
        mayor = len(palabra)
        larga = palabra
    elif len(palabra) < menor:
        menor = len(palabra)
        corta = palabra
    i = i + 1
print 'la palabra mas larga es ',larga
print 'la palabra mas corta es ',corta
    
