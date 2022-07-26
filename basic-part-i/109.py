#!/usr/bin/env python3

task = """
Task:
Write a Python program to check if a number is positive, negative or zero.
"""

print(task)

n = int(input("Enter number: "))

if n < 0:
    print(n, "is negative")
elif n == 0:
    print(n, "is zero")
else:
    print(n, "is positive")