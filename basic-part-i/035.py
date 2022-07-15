#!/usr/bin/env python3

task = """
Task:
Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
"""

print(task)

def eq_what(n1, n2):
    if n1 == n2 or n1 + n2 == 5 or abs(n1-n2):
        return True
    else:
        return False

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Task result: ", eq_what(a, b))