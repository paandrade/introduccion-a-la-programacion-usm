def calcular(numero_1,operador,numero_2):
    if operador == '+' :
        resultado = numero_1 + numero_2
        #return resultado
    elif operador == '-':
        resultado = numero_1 - numero_2
        #return resultado
    elif operador == '*':
        resultado = numero_1 * numero_2
        #return resultado
    elif operador == '/':
        resultado = numero_1 / numero_2
        #return resultado
    elif operador == '**':
        resultado = numero_1 ** numero_2
        #return resultado

    return resultado

num_1=int(raw_input('Operando: '))
opera=raw_input('ingrese operador: ')
num_2=int(raw_input('Operando: '))

print calcular(num_1,opera,num_2)
        
