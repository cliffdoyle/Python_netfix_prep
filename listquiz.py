"""
3. 5.3 (Fill in the Missing Code) Replace the ***s in the following list
comprehension and map function call, such that given a list of heights in
inches, the code maps the list to a list of tuples containing the original
height values and their corresponding values in meters. For example, if
one element in the original list contains the height 69 inches, the
corresponding element in the new list will contain the tuple (69,
1.7526), representing both the height in inches and the height in
meters. There are 0.0254 meters per inch.
[*** for x in [69, 77, 54]]
list(map(lambda ***, [69, 77, 54]))
"""

def generator_tup(x):
    return (x,x*0.0254)

listcomprehension=[generator_tup(x) for x in [69,77,54]]
print(listcomprehension)

mapinglistvals=list(map(lambda x: (x,x*0.0254),[69,77,54]))
print(mapinglistvals)

"""
    4. 5.4 (Iteration Order) Create a 2-by-3 list, then use a nested loop to:
1. Set each element’s value to an integer indicating the order in
which it was processed by the nested loop.
2. Display the elements in tabular format. Use the column indices
as headings across the top, and the row indices to the left of
each row.
    """
a=[[77, 68, 86, 73], # first student's grades
[96, 87, 89, 81], # second student's grades
[70, 90, 86, 81]]

for i,row in enumerate(a):
    # print(i)
    for j,num in enumerate(row):
        print(f'[{i}{j}]={num}',end=' ')
    print()
    
"""
5. 5.5 (IPython Session: Slicing) Create a string called alphabet
containing 'abcdefghijklmnopqrstuvwxyz', then perform the
following separate slice operations to obtain:
1. The first half of the string using starting and ending indices.
2. The first half of the string using only the ending index.
3. The second half of the string using starting and ending indices.
4. The second half of the string using only the starting index.
5. Every second letter in the string starting with 'a'.
6. The entire string in reverse.
7. Every third letter of the string in reverse starting with 'z'.
    """
alphabet='abcdefghijklmnopqrstuvwxyz'
print(alphabet[0:13])
print(alphabet[:13])
print(alphabet[13:len(alphabet)])
print(alphabet[13:])
print(alphabet[::2])
print(alphabet[::-1])
print(alphabet[::-3])

""" 
6. 5.6 (Functions Returning Tuples) Define a function rotate that
receives three arguments and returns a tuple in which the first argument
is at index 1, the second argument is at index 2 and the third argument is
at index 0. Define variables a, b and c containing 'Doug', 22 and
1984. Then call the function three times. For each call, unpack its result
into a, b and c, then display their values.
"""
def rotate(x,y,z):
    return(z,x,y)

a=['Doug',22,1984]
b=['Doug',22,1984]
c=['Doug',22,1984]
a=rotate('viola','nadia','eunice')
b=rotate('viola','nadia','eunice')
c=rotate('viola','nadia','eunice')

print(a)
print(b)
print(c)

"""
7. 5.7 (Duplicate Elimination) Create a function that receives a list and
returns a (possibly shorter) list containing only the unique values in
sorted order. Test your function with a list of numbers and a list of
strings.
    """
def duplicate_elimination(seq):
    res=[]
    for v in seq:
        
        if v not in res:
            res.append(v)
            # print(res)
    return sorted(res)

lis1=[19343536720,883930209,100432,356422,6755843,846456,124806]
lis2=['ker','hey','swee','hune']

print(duplicate_elimination(lis1))
print(duplicate_elimination(lis2))

