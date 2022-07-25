#!/usr/bin/env python3

task = """
Task:
Write a Python program to check whether a string is numeric.
"""

print(task)

def check_numeric(v):
    try:
        num = int(v)
        return True
    except:
        return False

s = input("Enter string: ")
print("String '{}' is numeric: {}".format(s, check_numeric(s)))