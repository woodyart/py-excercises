#!/usr/bin/env python3

task = """
Task:
Write a Python program to check whether a specified value is contained in a group of values.
"""

print(task)

def check_val(val, values):
    return val in values

values = [3,4,5,6,7,8,9]
a = int(input("Enter value: "))

print(a, "->", values, ":", check_val(a, values))