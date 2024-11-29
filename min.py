"""Find minimum of three values"""
num1=int(input('Enter first no: '))
num2=int(input('Enter second no: '))
num3=int(input('Enter third no: '))

minimum=num1

if num2<minimum:
    minimum=num2

if num3<num2:
    minimum=num3
    
print('Minimum number is',minimum)
print(min(12,34,2))
x=str(45)
print(x)
