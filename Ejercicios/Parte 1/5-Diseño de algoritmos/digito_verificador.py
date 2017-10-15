rol=int(raw_input('Ingrese rol: '))
rol = str(rol)

rol_inv=''

i = -1

while i >= -len(rol):
    rol_inv = rol_inv + rol[i]
    i = i - 1
print rol_inv

factor = 2
c = 0
suma = 0

while factor <= 7:
    suma1= int(rol_inv[c])*factor
    suma = suma + suma1
    factor = factor + 1
    c = c + 1
factor = 2
while factor <= 4:
    suma2 = int(rol_inv[c])*factor
    suma = suma + suma2
    factor = factor + 1
    c = c + 1

mod = suma%11

dv = 11 - mod

print 'el digito verificador es ',dv,' el rol completo es ',int(rol),'-',dv
