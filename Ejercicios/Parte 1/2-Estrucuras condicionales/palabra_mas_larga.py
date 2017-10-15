palabra_1=raw_input('Palabra 1: ')
palabra_2=raw_input('Palabra 2: ')

if len(palabra_1)>len(palabra_2):
    dif=len(palabra_1)-len(palabra_2)
    print 'La palabra ',palabra_1,' tiene ',dif,' letras mas que ', palabra_2

elif len(palabra_1)<len(palabra_2):
    dif=len(palabra_2)-len(palabra_1)
    print 'La palabra ',palabra_2,' tiene ',dif,' letras mas que ', palabra_1

else:
    print 'La dos palabras tienen el mismo largo'
