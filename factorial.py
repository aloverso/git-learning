# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:35:02 2015

@author: aloverso & Luciano
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
    if n<=1:
        return n
    return n * factorial(n-1)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
