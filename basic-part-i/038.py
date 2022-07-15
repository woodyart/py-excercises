#!/usr/bin/env python3

task = """
Task:
Write a Python program to solve (x + y) * (x + y).
"""

print(task)

def formula(n1, n2):
    s = (n1 + n2) ** 2
    return s

x = int(input("Enter X: "))
y = int(input("Enter Y: "))
print("({} + {})^2 = {}".format(x, y, formula(x, y)))