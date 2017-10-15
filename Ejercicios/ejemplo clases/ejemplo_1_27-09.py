#precio metro cuadrado 20 UF

# si area < 100 -> descuento de 25% al precio de m2

#si 100<=area<=1000 precio = 20% precio

area = int(raw_input('ingrese area: '))

c=0
total_a=0
total_b=0
total_c=0
mayor_a = -1
mayor_b = -1
mayor_c = -1


while area != 0:
    sector=raw_input('ingrese sector [a/b/c]: ')
    if sector == 'a':
        if area < 100:
            precio= 0.75*20*area
            print ' el precio de ',area,' m2 en sector A es ',precio
        elif 100 <= area <= 1000:
            precio = 1.2*20*area
            print ' el precio de ',area,' m2 en sector A es ',precio
        elif area > 1000:
            precio = 1.5*20*area
            print ' el precio de ',area,' m2 en sector A es ',precio
        total_a= total_a+precio
        if area>mayor_a:
            mayor_a=area

 
    if sector == 'b':
        if area < 100:
            precio= 0.75*20*area
            print ' el precio de ',area,' m2 en sector B es ',precio
        elif 100 <= area <= 1000:
            precio = 1.2*20*area
            print ' el precio de ',area,' m2 en sector B es ',precio
        elif area > 1000:
            precio = 1.5*20*area
            print ' el precio de ',area,' m2 en sector B es ',precio
        total_b= total_b+precio
        if area>mayor_b:
            mayor_b=area


    if sector == 'c':
        if area < 100:
            precio= 0.75*20*area
            print ' el precio de ',area,' m2 en sector C es ',precio
        elif 100 <= area <= 1000:
            precio = 1.2*20*area
            print ' el precio de ',area,' m2 en sector C es ',precio
        elif area > 1000:
            precio = 1.5*20*area
            print ' el precio de ',area,' m2 en sector C es ',precio
        total_c = total_c+precio
        if area>mayor_c:
            mayor_c=area

    area=int(raw_input('Ingrese area: '))
    
if area == 0:
    print 'fin programa'

print 'el area mayor de A es',mayor_a,'el total de area valuada es ', total_a

print 'el area mayor de B es',mayor_b,'el total de area valuada es ', total_b

print 'el area mayor de C es',mayor_c,'el total de area valuada es ', total_c
