#!/usr/bin/env python3

from math import sqrt


task = """
Task:
Write a Python program to calculate the hypotenuse of a right angled triangle.
"""

print(task)

def hypotenuse(a, b):
    return sqrt(a**2 + b**2)

print("""
  |\\
  | \\
A |  \\ C - Hypotenuse
  |   \\
  |____\\
    B
""")

a = float(input("Enter A-side length: "))
b = float(input("Enter B-side length: "))

print("The hypotenuse C =", round(hypotenuse(a, b), 2))