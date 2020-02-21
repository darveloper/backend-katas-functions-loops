#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "???"


def add(x, y):
    return x + y


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    if(y == 0): 
        return 0
  
    # Add x one by one  
    if(y > 0 ): 
        return add(x, multiply(x,y-1)) 
  
    # The case where y is negative 
    if(y < 0 ): 
        return -multiply(x, -y) 


def power(x, n):
    """Raise x to power n, where n >= 0"""
    if (n == 0): return 1
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
    else:
        w = factorial(x-1)
        return power(w, x)


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


if __name__ == '__main__':
    add(2, 4)
    multiply(6, -8)
    power(2, 8)
    factorial(4)
    fibonacci(8)

    pass
