#!/usr/bin/env python3

task = """
Task:
Write a Python program to add two objects if both objects are an integer type.
"""

print(task)

def sum_t(n1, n2):
    if isinstance(n1, int) and isinstance(n2, int):
        return n1 + n2        
    else:
        return False

def sum_print(n1, n2):
    s = sum_t(n1, n2)
    print(n1, "+", n2, "=", s) if s != False else print("Error:", n1, "and", n2, "must be integer")

sum_print(1, 2)
sum_print(3, '4')
sum_print("5", int("6"))