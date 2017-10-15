raw_input()

print'Potencia   ','Fraccion   ','Suma   '

fraccion = 1
suma = 0
potencia = 0


while fraccion > 0.000001:

    potencia = potencia + 1

    fraccion= ((1.0)/2)**potencia

    suma = suma + fraccion

    print potencia,'           ',fraccion,'            ',suma,'   '


