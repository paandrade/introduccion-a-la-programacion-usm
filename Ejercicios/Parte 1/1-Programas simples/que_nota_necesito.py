nota_1=int(raw_input('Ingrese nota certamen 1: '))
nota_2=int(raw_input('Ingrese nota certamen 2: '))
nota_lab=int(raw_input('Ingrese nota laboratorio: '))
nota_deseada=int(raw_input('Que nota final desea obtener: '))

nota_certamenes=(nota_deseada-0.3*nota_lab)/0.7

nota_3=(3*nota_certamenes) - nota_1 - nota_2

print 'Necesita nota ',nota_3,' en el certamen 3'
