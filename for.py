"""for loop in python"""

for ch in 'python':
    print(ch, sep=',')
    
    
# print(10, 20 ,30,)

for counter in range(12):
    print(counter, end='')
    
print()

#Class average 
"""Class average program with sequence-controlled iteration"""
#Initialization phase
total=0
grade_counter=0
grades=[98,76,71,87,83,90,57,79,82,94]

#processing phase
for grade in grades:
    total+=grade
    grade_counter+=1

#termination phase
average=total/grade_counter
print('Class average is',average)