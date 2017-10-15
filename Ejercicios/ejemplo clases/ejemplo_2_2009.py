import math

def perimetro(radio):
    perimetro=2*radio*math.pi
    return perimetro
def area(radio):
    area=(radio**2)*math.pi
    return area

radio_user=int(raw_input('ingrese radio: '))

print 'el perimetro es ',perimetro(radio_user),', y el area es ',area(radio_user)
