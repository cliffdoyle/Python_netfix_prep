import math

def area(r):
    a=math.pi*r**2
    return a

print(area(789))

def compare(x,y):
    if x > y:
        return 1
    if x==y:
        return 0
    if x < y:
        return -1
    

print(compare(23,7))