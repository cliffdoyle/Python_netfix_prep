#Sorting enables arranging data in ascending or descending order
#Sorting in ascending order
numbers=[10,3,7,1,9,4,2,8,5,6]
numbers.sort()
print(numbers)

#Sorting in descending Order
numbers.sort(reverse=True)
print(numbers)


##Built-in function sorted
#returns a new list containing the sorted elements of its argument sequence
#The original sequence is unmodified

#list
nembni=[10,3,7,1,9,4,2,8,5,6]
asce_nemb=sorted(nembni)
print(asce_nemb)
print(nembni)

#string
letters = 'fadgchjebi'
ascending_letters = sorted(letters)
print(ascending_letters)
print(letters)

#tuple
colors=('red','orange','yellow','green','blue')
asce_color=sorted(colors)
desc_color=sorted(colors,reverse=True,)
print(desc_color)
print(asce_color)
print(colors)