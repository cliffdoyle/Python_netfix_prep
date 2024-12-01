"""List comprehension: a concise and convenient notation for creating new lists"""
#List comprehensions can replace many for statements that iterate over existing sequences to create new lists
#i.e
list1=[]

for item in range(1,6):
    list1.append(item)

print(list1)

#Using a List Comprehension to create a List of Integers
#L.comp does the same thing in a single line of code

list2=[ite for ite in range(1,6)]
print(list2)

list3=list(range(1,6))
print(list3)

#Performing operations in a list Comprehension Expression
#We can perform calculations that map elements to new values
#The code maps each value to its cube with this expression: item**3

list3=[item **3 for item in range(0,7) ]#if item%2 !=0]
print(list3)

#Processing another list

colors=['red','purple','indigo','green']
colors2=[item.upper() for item in colors]

print(colors)
print(colors2)

#Generator Expressions
#Creates an iterable generator object that produces values on demand
#Also known as lazy evaluation which is different from greedy evaluation(creates list immediately) observed with list comprehension

numero=[10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

for value in (x**2 for x in numero if x%2 !=0):
    print(f' {value}',end='\n')
    
"""more on functional programming"""
#Just like data, functions in python can be assigned to variables
#pass to other functions and return from functions
def is_odd(x):
    """Returns true only if x is odd."""
    return x % 2 !=0

#Use built=in functions to obtain the odd values in numbers
#Filter is an example of a high order function
#Filter returns an iterator, filters results are not produced untill
#you iterate through them, function list iterates through the results and creates a list containing them
 
newlist=list(filter(is_odd,numero))
print(newlist)

#Obtaining same results using a list comprehension with an if clause:
compre=[item for item in numero if is_odd(item)]
print(compre)

#Using a lambda Rather than a function
#for simple functions like is_odd that return only a single expression's value
#we can utilize a lambda expression(simply lambda) to define the function inline where it's needed
#Any simple func of the form:
"""
    def function_name(parameter_list):
        return expression
may be expressed as a more concise lambda of the form 
    lambda parameter_list:expression
    """
    #A lambda begins with the lambda keyword followed by
    #a comma-separated parameter list, a colon(:), and an expression
lamfunc=list(filter(lambda x: x % 2 !=0,numero))
print(lamfunc)

#Mapping a Sequence's Values to New Values

newLis=list(map(lambda x: x**2,numero))
print(newLis)
#Equivalent list comprehension
samRes=[item**2 for item in numero]
print(samRes)

#Combining filter and map

#First, filter returns an iterable representing only the odd values of numbers. 
# Then map returns an iterable representing
#the squares of the filtered values. Finally, list uses map’s iterable to create the
#list.
combi=list(map(lambda x:x**2,
               filter(lambda x: x % 2 !=0,numero)))
print(combi)

#List Comprehension doing the same job!
#For each value of x in numbers, the expression x**2 is performed 
#only if the condition x % 2 !=0 is True
listcombi=[x**2 for x in numero if x % 2 !=0]
print(listcombi)

#Reduction :totaling the elements of a Sequence with sum
#Reduction process a sequence's elements into a single value
#Built in functions such as len,sum,min and max all do reduction

numsum=sum(numero)
print(numsum)

