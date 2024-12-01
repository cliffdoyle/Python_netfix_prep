#Creating a Two-Dimensional List
#A list with m rows and n columns is called an m-by-n list and has m × n elements.
a=[[77, 68, 86, 73], # first student's grades
[96, 87, 89, 81], # second student's grades
[70, 90, 86, 81]] # third student's grades

# for row in a:
#     for item in row:
        # print(item ,end=' ')
    # print()
    
#How the Nested Loops Execute
for i,row in enumerate(a):
    # print(i)
    # print(row)
    for j,item in enumerate(row):
        # print(j)
        print(f'a[{i}][{j}]={item}', end=' ')
    print()