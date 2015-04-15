# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:35:02 2015

@author: aloverso
"""

def factorial(n):
    total = 1
    for i in range(1,n+1):
        total = total*i 
    return total
