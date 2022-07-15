#!/usr/bin/env python3

from math import pi

task = """
Task:
Write a Python program to get the volume of a sphere with radius 6.
"""

print(task)

r = int(input("Enter sphere radius: ") or "6")
v = 4/3 * pi * r ** 3

print("The volume of sphere with radius", r, "is", v)