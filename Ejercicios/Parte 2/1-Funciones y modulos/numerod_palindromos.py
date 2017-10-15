def invertir_digitos(numero):
    numero = str(numero)
    num_inv = ''
    i = -1
    while i >= -len(numero):
        num_inv += numero[i]
        i = i - 1
    return int(num_inv)


num = int(raw_input('Ingrese n: '))

if num == invertir_digitos(num):
    print 'Es palindromo'
else:
    print 'No es palindromo'
