# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:35:02 2015

@author: aloverso
"""

def factorial(n):
    if n==1:
        return n
    return n * factorial(n-1)

