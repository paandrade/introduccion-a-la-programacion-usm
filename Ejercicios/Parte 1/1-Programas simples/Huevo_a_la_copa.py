# -*- coding: cp1252 -*-
import math
#huevo a la copa


#ingresar tamaño huevo
tamanio=int(raw_input('Tamaño huevo 1-Pequeño 2-Grande: '))

#Ingresar temperatura inicial huevo
temp=int(raw_input('Temperatura inicial del huevo: '))
temp_max=70
Pi=3.141592

prod_1= (3.7*(1.038**(0.33)))/((5.4e-3)*(Pi**2)*((4*Pi/3)**(0.66)))

prod_2=math.log(0.76*(temp-100)/(-30))
#prod_2=(temp - 100)
#prod_2=prod_2 / (-30)
#prod_2=prod_2 * 0.76
#prod_2=math.log(prod_2)


#operaciones si el huevo es pequeño
if tamanio == 1:
    t1= (47**(0.66))*prod_1*prod_2
    print 'El tiempo de coccion del huevo es de ',t1,' segundos'

#operaciones si el huevo es grande
if tamanio == 2:
    t2= (67**(0.66))*prod_1*prod_2
    print 'El tiempo de coccion del huevo es de ',t2,' segundos'

else:
    print 'incorrecto'


raw_input()
    
