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

cant_primo = int(raw_input('Cuantos primos: '))
i = 1
suma = 0

while suma < cant_primo :
    if primo(i):
        suma = suma + 1
        print i
    i = i + 1
