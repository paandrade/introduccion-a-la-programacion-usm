num=int(raw_input('ingrese numero: '))

num1= num//100
num2= (num%100)//10
num3= num%10

num_inv=(100*num3)+(10*num2)+(num1)

print num_inv

raw_input()
