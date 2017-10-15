def palindromo(palabra):
    palabra_inv = ''
    i = -1
    while i >= -len(palabra):
        palabra_inv = palabra_inv + palabra[i]
        i = i - 1
    if palabra_inv == palabra:
        return True
    else:
        return False
    return

palabra=raw_input('Ingrese palabra: ')

if palindromo(palabra):
    print 'Es palindromo'
else:
    print 'No es palindromo'
