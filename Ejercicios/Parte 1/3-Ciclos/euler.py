raw_input()

suma = 1.0
flag = True
i=0
divisor = 1.0

while flag == True :
    divisor= (i+1)*divisor
    suma = suma + (1.0/divisor)

    #dif = (1.0/divisor) - (1.0/((divisor)*(i+1)))

    #if dif < 0.000001:
    #    flag = False

    
    print suma
print suma
