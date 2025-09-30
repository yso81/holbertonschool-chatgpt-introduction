#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer recursively.

    Parameters:
        n (int): The non-negative integer to compute the factorial of.

    Returns:
        int: The factorial of the input integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
