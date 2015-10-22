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
    total = 1 # keeps track of the total
    for i in range(1,n+1):
        total = total*i # multiply the total times i
    return total # return the total
   

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True) # test our function
