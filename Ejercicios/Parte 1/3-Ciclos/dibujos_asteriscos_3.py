lado=int(raw_input('Lado: '))

tamano_lado=0
espacio=' '

fila=''

while tamano_lado < lado :
    tamano_lado += 1
    fila = fila+'*'
    espacio = espacio + ' '
    if espacio > 0:
        fila_f= espacio +fila
        print fila_f
