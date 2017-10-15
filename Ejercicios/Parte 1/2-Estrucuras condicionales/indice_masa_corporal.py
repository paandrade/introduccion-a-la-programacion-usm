print 'Calculador de masa corporal'

peso = float(raw_input('Ingrese su peso [kg]: '))
estatura_cm = float(raw_input('ingrese su estatura [cm]: '))
edad = int(raw_input('Ingrese su edad: '))

estatura_m = estatura_cm/100

imc = peso / (estatura_m**2)

if edad < 45:
    if imc < 22.0:
        riesgo = 'bajo'
    elif imc >= 22.0:
        riesgo = 'medio'
if edad >= 45:
    if imc < 22.0:
        riesgo = 'medio'
    elif imc >= 22.0:
        riesgo = 'alto'

print 'Su IMC es ',imc,' ,por lo tanto, tiene  riesgo ',riesgo,' de sufrir enfermedades cardiacas'
