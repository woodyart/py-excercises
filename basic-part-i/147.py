#!/usr/bin/env python3

task = """
Task:
Write a Python function to check whether a number is divisible by another number.
Accept two integers values form the user.
"""

print(task)

n = int(input("Enter number: "))
d = int(input("Enter divisor: "))

if n%d == 0: print("{} divisible by {}".format(n, d))
else: print("{} is not divisible by {}".format(n, d))