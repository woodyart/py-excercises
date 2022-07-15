#!/usr/bin/env python3

task = """
Task:
Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""

print(task)

def within (number):
    return ((abs(1000 - number) <= 100 or abs(2000 - number) <= 100))

x = int(input("Enter number: "))
print("Entered number", x, "is within 100 of 1000 or 2000:", within(x))