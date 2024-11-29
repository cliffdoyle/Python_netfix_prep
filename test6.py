"""more recursive functions"""


def factorial(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n <0:
        print('Factorial is not defined for negative integers.')
        return None
    if n==0:
        return 1
    else:
        recurse=factorial(n-1)
        result=n*recurse
        return result

print(factorial(1.0))

def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        recurse=fibonacci(n-1)+fibonacci(n-2)
        return recurse
    
print(fibonacci(63))