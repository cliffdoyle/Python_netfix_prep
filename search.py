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

#Other List Methods
##Methods that add and remove elements

color_names=['orange','yellow','green']
#Method insert adds a new item at a specified index
#The code inserts red at index 0

color_names.insert(5,'pink')
print(color_names)

##Method append
#Adds a new item to the end of a list
color_names.append('blueberry')
print(color_names)

#Adding all the elements of a sequence to the end of a list
#Method extend adds all the elements of another sequence to the end of a list

color_names.extend(['indigo','violet','cream','white'])
print(color_names)

#Using extend is equivalent to using the augmented += operator
sample_list=[]
s='abcdef'
sample_list.extend(s)
print(sample_list)
t=(1,2,4,'hello')
sample_list.extend(t)
print(sample_list)
#passing tuple directly to extend
sample_list.extend((4,5,6))
print(sample_list)

#Removing the first occurrence of an element in a list
#ValueError occurs if removes argument is not in the list

color_names.remove('blueberry')
print(color_names)

#Emptying a list with method clear
# color_names.clear()#equivalent of color_names[:]=[]
print(color_names)

#Counting the number of Occurrences of an Item
#List method count searches for its argument and returns the number of times it is found
responses=[1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 2]

for i in range(1,6):
    print(f'{i} appears {responses.count(i)} times in responses')
    
#Reversing a Lists Elements
#method reverse reverses the contents of a list in place 
color_names.reverse()
print(color_names)

#Copying a List
#Method copy returns a new list containing a shallow copy of the original list
copied_list=color_names.copy()#equivalent to coplist=color_names[:]
print(copied_list)