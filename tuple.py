"""tuple in python"""

tup1=(1,2,3,5)
print(tup1[-2])

#Creating tuple
student_tuple=()
print(len(student_tuple))

#Unpacking from string, list and tuples

first, second='ho'
print(f'{first} {second}')

num1, num2=[2,9]
print(f'{num1} {num2}')

numz1,numz2=range(2,4)
print(f'{numz1} {numz2}')

#Swapping values via packing and unpacking
numerouno=104
numero2=67

numerouno,numero2=(numero2,numerouno)

print(f'numerouno={numerouno};numero2={numero2}')

#Utilizing inbuilt enumerate func to get index and value

colors=['purple','yellow','green','white','indigo']
print(list(enumerate(colors)))
print(tuple(enumerate(colors)))

for index,value in enumerate(colors):
    print(f'{index}:{value}')
    

"""Displaying a bar chart"""
nombers=[19,24,5,40,34]

print('\nCreating a bar chart from numbers:')
print(f'Index{"Value":>8} Bar')

for index,value in enumerate(nombers):
    print(f'{index:>5}{value:>8}  {"*"*value}')
    
#Sequence slicing
##You can slice sequences to create new sequences of the same type containing subsets
#of the original elements
#Slice operations can modify mutable sequences 

#specifying a Slice with starting and Ending Indices
nums=[2,3,5,7,11,13,17,19]
print(f'\n {nums[2:6]}')#copies elements from starting index upto but not including the ending index. original list isn't modified

#Specifying a slice with only an Ending Index
#if you omit starting index, 0 is assumed
#Slice [:6] equivalent to slice [0:6]

print(f'\n {nums[:8]}')

#Specifying a Slice with Only a Starting Index
#If you omit the ending index, python assumes the sequence's length
print(f'\n {nums[6:]}')

#Specifying a slice with No Indices
#Omitting both the start and end indices copies the entire sequence
print(f'\n {nums[:]}')

#Slicing with Steps
#Creating a slice with a step of 2
print(f'\n {nums[0:8:2]}')#saame as nums[::2]

#Slicing with Negative Indices and Steps
#You can use a negative step to select slices in reverse order
print(f'\n {nums[-1:-8:-1]}')

#Modifying lists via Slices

#The code replaces the lists first three elements leaving the rest unchanged
nums[0:3]=['two','three','five']
print(f'\nnewNums={nums}')

#The code below deletes only the specified elements by assigning an empty list to them
nums[0:3]=[]
print(f'\ndeletedFirstThree={nums}')

#Using del statement to remove elements from a list
newnumb=list(range(0,7))
print(f'\n {newnumb}')
del newnumb[-1]
print(f'\n {newnumb}')

#Deleting a Slice from a List
#The code deletes the list first two elements
del newnumb[0:2]
print(f'\n newlist={newnumb}')

#Use step to delete every other element from list
del newnumb[::2]

print(f"\n stepDeletion={newnumb}")

#Deleting a slice representing the entire list
del newnumb[:]
print(newnumb)

#Passing Lists to Functions
#What happens when a program passes a mutable list object to a function
def modify_elements(items):
    """multiplies all element values in items by 2"""
    for i,v in enumerate(items):
        items[i]*=2
        # print(v)
      
        
        

numq=[10,3]
numq.append(8)
modify_elements(numq)
print(f'modifiedEle={numq}')

#Passing a Tuple to a Function
# numk=(10,30)
# modify_elements(numk)
# print(f'modifiedEle={numk}')#This operation results in TypeError as Tuple is immutable
