#!/usr/bin/env python3

from math import sqrt

task = """
Task:
Write a Python program to get the third side of right angled triangle from two given sides.
"""

print(task)

def get_triangle_side(a, b, c):
    if   str(a) == 'x':
        x = round(sqrt(int(b)**2 - int(c)**2), 2)
        return x, b, c
    elif str(b) == 'x':
        x = round(sqrt(int(a)**2 + int(c)**2), 2)
        return a, x, c
    elif str(c) == 'x':
        x = round(sqrt(int(b)**2 - int(a)**2), 2)
        return a, b, x
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
  {:>3}|  \\ {:<3}
     |   \\
     |____\\
      {:>3}

    """.format(a, b, c))

a, b, c = input_values()
a, b, c = get_triangle_side(a, b, c)
print_triangle(a, b, c)