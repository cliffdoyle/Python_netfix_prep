"""more built in functions for manipulating sequences"""
#Finding the Minimum and Maximum Values Using a Key Function
'Red'<'orange'
#expression above is true because strings are compared by there 
#underlying numerical values, lowercase letters have higher numerical values 
#than uppercase

print(ord('R'))
print(ord('o'))
#ord returns the numerical value of a character
colors = ['Red', 'orange', 'Yellow', 'green', 'Blue']
#to compare this strings we must first convert all of them to lowercase
#since python compares strings using numerical values
mincolor=min(colors,key=lambda s: s.lower())
maxcolor=max(colors,key=lambda s:s.lower())
print(mincolor)
print(maxcolor)
#The key keyword argument must be a one-parameter function that returns a value.
#In this case, it’s a lambda that calls string method lower to get a string’s lowercase version. 
# Functions min and max call the key argument’s function for each element and use the results to
#compare the elements.

#Iterating Backward Through a Sequence
#Built-in function reversed returns an iterator that 
#enables you to iterate over a sequence's values backward
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

reversed_numbers=[item**2 for item in reversed(numbers)]
print(reversed_numbers)

#Combining Iterables into Tuples of Corresponding Elements
#Built in func zip enables you to iterate over multiple iterables of data at same time.
#It receives as arguments any no of iterables and returns an iterator
#that produces tuples containing the elements at the same index in each
names = ['Bob', 'Sue', 'Amanda']
grade_point_averages = [3.5, 4.0, 3.75]

for name,gpa in zip(names,grade_point_averages):
    print(f'Name={name} : GPA={gpa}')#we unpack each tuple into name and gpa and display them

