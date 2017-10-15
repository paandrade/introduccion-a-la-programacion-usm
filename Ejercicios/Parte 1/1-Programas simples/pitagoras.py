cateto_a=int(raw_input('ingrese cateto a: '))
cateto_b=int(raw_input('ingrese cateto b: '))

hip= ((cateto_a**2)+(cateto_b**2))**0.5

print 'La hipotenusa es ',hip

print "  |\ "
print "  | \ "
print cateto_a,"|  \ ",hip
print "  |   \ "
print "  |____\ "
print '   ',cateto_b
raw_input()
