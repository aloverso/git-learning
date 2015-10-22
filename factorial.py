# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:35:02 2015

@author: aloverso & Luciano & sarahwalters
"""

# Calculates the factorial of a number
def factorial(n):
    """
    Testing the factorial
    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """
    if n == 1: # base case
        return 1
    else:
        return n*factorial(n-1) # recurse

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True) # test our function
