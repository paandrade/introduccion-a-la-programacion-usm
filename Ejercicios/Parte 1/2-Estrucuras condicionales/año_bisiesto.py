ano=int(raw_input('Ingrese anio: '))

cond_1=ano%4
cond_2=ano%100 
cond_3=ano%400

if cond_2==0 and cond_3==0:
    print 'el ',ano,' es bisiesto'

elif cond_2==0 and cond_3!=0:
    print 'el ',ano,' no es bisiesto'

elif cond_1==0 and cond_3!=0:
    print 'el ',ano,' es bisiesto'
