#pedir hora actual
hora_actual=int(raw_input('Hora actual: '))

#pedir cantidad horas futuras
hora_fut=int(raw_input('Cantidad de horas: '))

if hora_fut%24==0:
    print 'En ',hora_fut,' horas, el reloj marcara las ',hora_actual,' horas'

if hora_fut<24:
    if (hora_fut+hora_actual)%24!=0:
        print 'En ',hora_fut,' horas, el reloj marcara las ',(hora_fut+hora_actual)%24,' horas'
    if (hora_fut+hora_actual)%24==0:
        print 'En ',hora_fut,' horas, el reloj marcara las ',(hora_fut+hora_actual)%24==0,' horas'

if hora_fut>24:
    if (hora_fut+hora_actual)%24!=0:
        print 'En ',hora_fut,' horas, el reloj marcara las ',(hora_fut+hora_actual)%24,' horas'
    if (hora_fut+hora_actual)%24==0:
        print 'En ',hora_fut,' horas, el reloj marcara las ',(hora_fut+hora_actual)%24,' horas'
