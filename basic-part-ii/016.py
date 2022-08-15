#!/usr/bin/env python3

from math import sqrt

task = """
Task:
Write a Python program to get the third side of right angled triangle from two given sides.
"""

print(task)

def get_triangle_side(a, b, c):
    if   str(a) == 'x':
        a = sqrt(b**2 - c**2)
    elif str(b) == 'x':
        b = sqrt(a**2 + c**2)
    elif str(c) == 'x':
        c = sqrt(b**2 - a**2)
    else:
        return a, b, c

def input_values():
    print("""
    
     |\\
     | \\
    A|  \\ B
     |   \\
     |____\\
        C

    """)
    return input("Enter A, B, C values separated by comma (x for unknown side): ").split(',')

def print_triangle(a, b, c):
    print("""

     |\\
     | \\
    {}|  \\ {}
     |   \\
     |____\\
        {}

    """.format(a, b, c))

a, b, c = input_values()
a, b, c = get_triangle_side(a, b, c)
print_triangle(a, b, c)