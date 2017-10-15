numero=int(raw_input('ingrese numero: '))

producto=1
i=1

if numero==0:
    producto=producto

else:
    while i <= numero:
        producto=producto*i
        i = i + 1
print producto
