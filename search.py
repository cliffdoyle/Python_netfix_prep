numbers=[3, 7, 1, 4, 2, 8, 5, 6]

numbers*=2
print(numbers)

#List method index
#Takes as an argument a search key(value to locate in the list),,searches through the list from index 0 
#returns index of the first element that matches the search key

iun=numbers.index(8)
print(iun)

#Specifying the starting Index of a search
q=numbers.index(7,6)
print(q)

#Specifying the Starting and Ending Indices of a search
#Causes index to search from the starting index up to 
#but not including the ending index location

#numbers.index(5,7) equivalent to numbers.index(5,7, len(numbers))
#The code below looks for value 7 in the range of elements with indices 0 through 3
k=numbers.index(7,0,4)
print(k)

#Operators in and not in 

##Operator in tests whether its right operand's iterable
##contains the left operand's value

print(1000 in numbers)

##Operator not in tests whether its right operands iterable does not
#contain left operands value

print(100 not in numbers)

##Using Operator in to prevent a ValuedError
key=8
if key in numbers:
    print(f'found {key} at index {numbers.index(key)}')
else:
    print(f'{key} not found')
    
print(all(numbers))