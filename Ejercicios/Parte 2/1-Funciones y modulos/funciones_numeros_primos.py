def es_divisible(n,d):
    if n%d == 0:
        return True
    else:
        return False
    return

def es_primo(numero):
    i = 1
    c = 0
    while i <= numero:
        if es_divisible(numero,i):
            c = c + 1
            i = i + 1
        else:
            i = i + 1
    if c == 2:
        return True
    else:
        return False
    return

def i_esimo_primo(i_primo):
    suma = 0
    i = 0
    while suma < i_primo:
        i = i + 1
        if es_primo(i):
            suma = suma + 1   
    return i
    
def primeros_primos(m):
    i = 1
    lista = []
    while i <= m:
        lista.append(i_esimo_primo(i))
        i = i + 1
    return lista

def primos_hasta(m):
    i = 1
    lista = []
    while i <= m:
        if es_primo(i):
            lista.append(i)
        i = i + 1
    return lista
    
