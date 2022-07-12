#!/usr/bin/env python3

from math import pi

task = """
Task:
Write a Python program which accepts the radius of a circle from the user and compute the area.
"""

print(task)

def isfloat(num):
    try:
        float(num)
        a = pi * float(r) ** 2
        print("Circle area is", a)
    except ValueError:
        print("Unknown value type", r)

r = input("Enter radius: ")

isfloat(r)