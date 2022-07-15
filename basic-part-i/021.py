#!/usr/bin/env python3

task = """
Task:
Write a Python program to find whether a given number (accept from the user) is even or odd,
print out an appropriate message to the user.
"""

print(task)

def isodd(num):
    if (num % 2) == 0:
        return False
    else:
        return True

x = int(input("Enter number: "))

if isodd(x):
    print(x, "is odd")
else:
    print(x, "is even")