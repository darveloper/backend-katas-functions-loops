def add(x, y):
    return x + y


print(add(2, 2))


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    if y < 0:
        return -multiply(x, -y)
    elif y == 1:
        return x
    elif y == 0:
        return 0
    else:
        return add(x, multiply(x, y-1))


print(multiply(3, 5))


def power(x, n):
    """Raise x to power n, where n >= 0"""
    if (n == 0):
        return 1
    elif (n % 2) == 0:
        one = power(x, int(n / 2))

        return multiply(one, one)
    else:
        one = power(x, int(n / 2))
        return multiply(x, multiply(one, one))
print(power(2, 3))


def factorial(x):
    """Compute factorial of x, where x > 0"""
    if x == 0:
        return 1
    else:
        return power(factorial(x-1), x)
        
print(factorial(4))

def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        one = fibonacci(n-1)
        two = fibonacci(n-2)
        return add(one, two)

print(fibonacci(8))
