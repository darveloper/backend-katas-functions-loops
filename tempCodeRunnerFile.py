def factorial(x):
    """Compute factorial of x, where x > 0"""
    if x == 1:
        return 1
    else:
        for n in range(x,1,-1):
            x = multiply(x,n-1)
        print(x)
factorial(2)

def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return add(fibonacci(n-1),fibonacci(n-2))

print(fibonacci(9))
