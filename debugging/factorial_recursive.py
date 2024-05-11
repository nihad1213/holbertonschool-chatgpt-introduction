#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number recursively.

    Function Description:
    ---------------------
    This function calculates the factorial of a given number using a recursive approach.
    The factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n.
    The factorial of 0 is defined as 1.

    Parameters:
    -----------
    n : int
        The number for which the factorial is to be calculated.

    Returns:
    --------
    int
        The factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the input from command line argument, calculate the factorial, and print the result
f = factorial(int(sys.argv[1]))
print(f)

