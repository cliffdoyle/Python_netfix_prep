"""more on strings"""

fruit='banana'
# fruit[3]='7'
# print(fruit)

index=0

# while index<len(fruit):
#     print(fruit[index])
#     index+=1

for i in fruit:
    print(i)
    
prefix='JKLMNOPQ'
suffix='ack'

for l in prefix:
    if l =='O' or l=='Q':
        print(l+'u'+suffix)
    else:
        print(l+suffix)
        
"""Slicing strings"""
s='Monty Python'
# print(s[0:4])

"""search implementation"""

def search(word, index,letter):
    count=0
    while index<len(word):
        count+=1
        print(count)
        if word[index]==letter:
            return index
        index+=1
    return -1

word='parrallel'
index=0
letter='l'
print(search(word,index,letter))

fu='rabolo'
count=0
for l in fu:
    if l=='o':
        count+=1
# print(count) 

def count(word,lett):
    count=0
    for l in word:
        if lett==l:
            count+=1
    return count
 
l='a'
fu='banana'   
# print(count(fu,l))

# print(fu.find('na',3))

"""the in operator"""

x='see'in'arkansas'
print(x)

def in_both(w1,w2):
    for l in w1:
        if l in w2:
            print(l)
            
in_both('connan','cabras')

t=[1,23,89,90,]
print(sum(t))
del t[2]
print(t)

s='spam.is.no.good'
t=s.split('.')
print(t)

x='   '.join(t)
print(x)
print(t is t)

"""more on list"""

t1=[1,2]
t2=t1.append(3)

print(t1)
print(t2)