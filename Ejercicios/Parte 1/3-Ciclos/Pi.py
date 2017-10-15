n = int(raw_input('n: '))

i = 0
suma = 0.0

while i < n:
    c=(-1)**i
    division = (1.0/(1+(2*i)))
    suma = suma + c*division
    i = i+1




print 4*suma
