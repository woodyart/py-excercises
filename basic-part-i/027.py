#!/usr/bin/env python3

task = """
Task:
Write a Python program to concatenate all elements in a list into a string and return it.
"""

print(task)

def concat(list):
    s = ""
    for item in list:
        s += str(item)
    return s

a = [ 1, "hello", '\t', "world", 2, 3 ]

print(a)
print(concat(a))