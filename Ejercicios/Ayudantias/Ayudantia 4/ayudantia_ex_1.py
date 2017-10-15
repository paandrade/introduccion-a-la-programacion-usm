l = [31,28,31,30,31,30,31,31,30,31,30,31]

def dia_siguiente((fecha)):
    anio,mes,dia=fecha
    if dia < l[mes-1]:
        dia = dia + 1
    elif dia == l[mes-1]:
        if mes < 12:
            dia = 1
            mes = mes + 1
        else :
            dia = 1
            mes = 1
            anio = anio +1

    return (anio,mes,dia)
