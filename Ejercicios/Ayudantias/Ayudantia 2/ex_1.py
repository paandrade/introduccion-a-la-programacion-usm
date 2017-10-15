n1=int(raw_input('primer numero; '))
n2=int(raw_input('segundo numero; '))
n3=int(raw_input('tercer numero; '))

if n1 == n2 == n3:
    print n1,n2,n3,' son iguale'
elif n1 <= n2 <= n3:
    print n3,n2,n1

elif n1 <= n3 <= n2:
    print n2,n3,n1

elif n2 <= n3 <= n1:
    print n1,n3,n2

elif n2 <= n1 <=n3:
    print n3,n1,n2

elif n3 <= n1 <= n2:
    print n2,n1,n3

elif n3 <= n2 <= n1:
    print n1,n2,n3
