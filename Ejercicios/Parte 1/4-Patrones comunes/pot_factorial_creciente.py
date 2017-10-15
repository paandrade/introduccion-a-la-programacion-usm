numero = int(raw_input('ingrese numero: '))
potencia= int(raw_input('ingrese potencia: '))

i = 0
producto=1

while i < potencia:
    producto = producto*(numero + i)
    i = i + 1
print producto
