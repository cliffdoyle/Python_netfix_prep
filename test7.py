"""iteration in python3"""


def countdown(n):
    if not isinstance(n,int):
        print('not valid int')
        return None
    while n > 0:
        print('good stuff')
        n-=2
    print('Blast off!')

# countdown(5)

while True:
    line=input('>')
    if line=='done':
        break
    # print(line)
print('Done')


