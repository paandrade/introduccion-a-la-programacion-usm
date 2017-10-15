n=int(raw_input('cantidad de datos: '))

mayor=-float("inf")
menor= float("inf")

c=0

while c<n:
    valor=int(raw_input('ingrese valor :'))
    if valor>mayor:
        mayor=valor
    if valor<menor:
        menor=valor
    c=c+1

rango=mayor-menor

print 'el rango es ',rango
