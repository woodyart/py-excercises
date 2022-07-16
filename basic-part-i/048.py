#!/usr/bin/env python3

task = """
Task:
Write a Python program to parse a string to Float or Integer.
"""

print(task)

def is_float(a):
    try:
        float(a)
        return True
    except:
        return False

val = input("Enter value: ")

if is_float(val):
    print("Value {} is float. Also it can be integer - {}".format(float(val), int(float(val))))
else:
    print("Value '{}' neither float nor integer".format(val))