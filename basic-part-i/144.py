#!/usr/bin/env python3

task = """
Task:
Write a Python program to check whether variable is integer or string.
"""

print(task)

for i in 123, "foo", 1.55:
    if isinstance(i, int): print(i, 'is integer')
    elif isinstance(i, str): print(i, 'is string')
    else: print(i, 'is not integer nor string')