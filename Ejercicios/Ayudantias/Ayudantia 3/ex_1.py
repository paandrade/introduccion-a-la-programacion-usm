#funciones
def costo_transito(min_comb):
          if min_comb <= 480:
                    return 0
          
          else :
                    horas = (min_comb/60)-8
                    minutos= min_comb%60
                    if minutos > 0:
                              return horas*5000 + 5000
                    else:
                              return horas*5000
                    
def costo_pasajero(hrs_viaje, costo_base, min_comb):
          costo= (hrs_viaje*30000) + (costo_base) + (costo_transito(min_comb))

          return costo
          
#programa

of_vuelo=raw_input('Vuelo: ')
menor= float("inf")
mejor_oferta=0

while of_vuelo != '':
          horas=int(raw_input('Horas: '))
          minutos_comb= int(raw_input('Minutos de combinacion: '))
          costo_base= int(raw_input('Costo base: '))

          costo_vuelo = costo_pasajero(horas,costo_base,minutos_comb)

          if costo_vuelo<menor:
                    menor=costo_vuelo
                    mejor_oferta= of_vuelo
          
          of_vuelo=raw_input('Vuelo: ')

print 'mejor vuelo: ',mejor_oferta
print 'costo pasajero: ',menor
