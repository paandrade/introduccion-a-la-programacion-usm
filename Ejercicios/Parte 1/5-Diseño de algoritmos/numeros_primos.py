def primo(numero):
    i = 1
    contador= 0
    while i <= numero:
        if numero % i == 0:
            contador += 1
        i = i + 1

    if contador == 2:
        return True
    else:
        return False
    return

numero = int(raw_input('Ingrese un numero: '))

if primo(numero):
    print numero,'es primo'
else:
    print numero,'es compuesto'
