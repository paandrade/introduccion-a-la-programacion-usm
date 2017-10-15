# ganar un set
#   condiciones:
#       ganar 6 juegos
#       ganar por lo menos 2 puntos

#se esta empatado a 5
#   gana el primero que llegue a 7 puntos

#se esta empaatado a 6
#   se define en ultimo juego, se gana por 7-6

juegos_ganados_a = int(raw_input('Juegos ganados por A: '))
juegos_ganados_b = int(raw_input('Juegos ganados por B: '))

diferencia_ab = juegos_ganados_a - juegos_ganados_b
diferencia_ba = juegos_ganados_b - juegos_ganados_a
#cuado aun no termina

if juegos_ganados_a<6 and juegos_ganados_b<6:
    print 'aun no termina'
elif juegos_ganados_a == 6 and juegos_ganados_b == 5 or juegos_ganados_b == 6 and juegos_ganados_a == 5:
    print 'aun no termina'    

# cuando B gana

elif juegos_ganados_b == 6 and juegos_ganados_a < 5 :
    print 'Gano B'
elif juegos_ganados_b == 7 and juegos_ganados_a == 6 :
    print 'gano b'

elif juegos_ganados_b == 7 and juegos_ganados_a == 5 :
    print 'ganno B'

# cuando A gana

elif juegos_ganados_a == 6 and juegos_ganados_b < 5 :
    print 'Gano A'

elif juegos_ganados_a == 7 and juegos_ganados_b == 6 :
    print 'gano a'

elif juegos_ganados_a == 7 and juegos_ganados_b == 5 :
    print 'ganno A'

else:
    print 'Invalido'


