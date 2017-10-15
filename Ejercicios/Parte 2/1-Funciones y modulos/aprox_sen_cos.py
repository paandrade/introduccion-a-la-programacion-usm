from math import sin

def factorial_reciproco(n):
    i = 0
    producto = 1
    while i < n :
        producto = producto*(i + 1)
        i = i + 1
    return 1/float(producto)

def signo(n):
    if n%2 == 0:
        return 1
    else:
        return -1
    return

def seno_aprox(x,m):
    suma = 0
    i = 0
    while i < m:
        suma = suma + signo(i)*(x**(2*i+1))*factorial_reciproco(2*i+1)
        i = i + 1
    return suma

def coseno_aprox(x,m):
    suma = 0
    i = 0
    while i < m :
        suma = suma +signo(i)*(x**(2*i))*factorial_reciproco(2*i)
        i = i + 1
    return suma

def error(f_exacta,f_aprox,m,x):
    dif = f_exacta(x)-f_aprox(x,m)
    return dif
