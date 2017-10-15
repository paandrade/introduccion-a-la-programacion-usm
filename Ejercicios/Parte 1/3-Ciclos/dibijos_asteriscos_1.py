altura=int(raw_input('Altura: '))
ancho=int(raw_input('Ancho: '))

an=0
al=0

linea=''

while an < ancho:
    linea=linea+'*'
    an=an+1
while al < altura:
    print linea
    al = al +1
    
