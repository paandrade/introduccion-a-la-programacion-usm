def palindromo(numero):
    numero = str(numero)
    num_inv = ''
    i = -1
    while i >= -len(numero):
        num_inv = num_inv + numero[i]
        i = i - 1
    if int(numero) == int(num_inv):
        return True
    else:
        return False
    return

numero = int(raw_input('Ingrese un numero: '))

if palindromo(numero):
    print str(numero)+' es palindromo'
else:
    print str(numero)+' no es palindromo'
