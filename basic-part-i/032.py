#!/usr/bin/env python3

from math import lcm

task = """
Task:
Write a Python program to get the least common multiple (LCM) of two positive integers.
"""

print(task)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

g = lcm(a,b)

print("LCM of", a, "and", b, "is", g)