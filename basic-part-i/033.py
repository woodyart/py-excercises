#!/usr/bin/env python3

task = """
Task:
Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
"""

print(task)

def sum_t(n1, n2, n3):
    if n1 == n2 or n1 == n3 or n2 == n3:
        return 0
    else:
        return n1 + n2 + n3

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Sum: ", sum_t(a, b, c))