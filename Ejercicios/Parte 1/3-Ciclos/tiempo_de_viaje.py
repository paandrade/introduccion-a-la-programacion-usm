duracion=int(raw_input('Duracion tramo: '))
suma=0
while duracion != 0 :
    suma= suma + duracion

    duracion = int(raw_input('Duracion tramo: '))

if duracion == 0:
    hora = suma/60
    minutos = suma%60

    print 'Tiempo total de viaje : ',hora,':',minutos,' horas'
