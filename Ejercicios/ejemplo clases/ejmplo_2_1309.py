n=int(raw_input('cuantos numero?: '))
c=0
mayor=-float("inf")
while c<n:
    num=float(raw_input('ingrese numero:')) 
    if num>mayor:
        mayor=num
    c+=1
print 'el numero mayor es',mayor
