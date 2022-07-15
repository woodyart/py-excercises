#!/usr/bin/env python3

from math import gcd

task = """
Task:
Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
"""

print(task)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

g = gcd(a,b)

print("GCD of", a, "and", b, "is", g)