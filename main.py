#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """
import sys

__author__ = "???"


def add(x, y):
    return x + y


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    if(y == 0):
        return 0

    # Add x one by one
    if(y > 0):
        return add(x, multiply(x, y-1))

    # The case where y is negative
    if(y < 0):
        return -multiply(x, -y)


def power(x, n):
    """Raise x to power n, where n >= 0"""
    if (n == 0):
        return 1
    elif (int(n % 2) == 0):
        return (power(x, int(n / 2)) *
                power(x, int(n / 2)))
    else:
        return (x * power(x, int(n / 2)) *
                power(x, int(n / 2)))


def factorial(x):
    """Compute factorial of x, where x > 0"""
    if x == 0:
        return 1
    i = 1
    n = 1
    while i <= x:
        n = multiply(n, i)
        i += 1
    return n


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


def main():
    if len(sys.argv) != 2:
        print(
            'usage: python main.py {--add | --multiply | --power | --factorial | --fibonacci}')
        sys.exit(1)

    option = sys.argv[1]
    if option == '--add':
        print(add(2, 4))
    elif option == '--multiply':
        print(multiply(6, -8))
    elif option == '--power':
        print(power(2, 8))
    elif option == '--factorial':
        print(factorial(4))
    elif option == '--fibonacci':
        print(fibonacci(8))
    else:
        print('unknown option: ') + option
        sys.exit(1)


if __name__ == '__main__':
    main()

    pass
