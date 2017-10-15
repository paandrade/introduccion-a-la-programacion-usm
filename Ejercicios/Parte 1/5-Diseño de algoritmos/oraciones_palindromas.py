def or_palindroma(oracion):
    i = 0
    ora=''
    while i < len(oracion):
        if oracion[i] != ' ':
            ora = ora + oracion[i]
            i = i + 1
        else:
            i = i + 1


    or_inv = ''
    i = -1
    while i >= -len(oracion):
        if oracion[i] != ' ':
            or_inv = or_inv + oracion[i]
            i = i - 1
        else:
            i = i - 1

    if or_inv == ora:
        return True
    else:
        return False
    return

oracion = raw_input('Ingrese oracion: ')

if or_palindroma(oracion):
    print 'Es palindromo'
else:
    print 'No es palindromo'
