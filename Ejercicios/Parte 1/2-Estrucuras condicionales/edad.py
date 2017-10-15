from time import localtime

t = localtime()

print 'Ingrese su fecha de nacimiento'

day = int(raw_input('Dia: '))
month = int(raw_input('Mes: '))
year = int(raw_input('Anno: '))

if month > t.tm_mon :
    edad = t.tm_year - year -1

elif month < t.tm_mon:
    edad = t.tm_year - year

elif month == t.tm_mon:
    if day <= t.tm_mday:
        edad = t.tm_year - year
    elif day > t.tm_mday:
        edad = t.tm_year - year -1

print 'Usted tiene ',edad,' annos'
    
