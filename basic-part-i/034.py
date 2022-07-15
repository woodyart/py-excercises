#!/usr/bin/env python3

task = """
Task:
Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
"""

print(task)

def sum_t(n1, n2, n3):
    s = n1 + n2 + n3
    if 15 <= s <= 20:
        return 20
    else:
        return s

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Sum: ", sum_t(a, b, c))