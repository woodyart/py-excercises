#!/usr/bin/env python3

task = """
Task:
Write a Python program to create the combinations of 3 digit combo.
"""

print(task)

print("All possible 3 digit combinations:")
for i in range(1000):
    s = str(i).zfill(3)
    if len(set(s)) == 1:
        print(s,"- COMBO!")
    else:
        print(s)