#!/usr/bin/env python3
'''
Python variable annotation
'''
def add(a: float, b: float) -> float:
    '''function adds two numbers of type float'''
    return a + b

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)
