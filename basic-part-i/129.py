#!/usr/bin/env python3

task = """
Task:
Write a Python program to add leading zeroes to a string.
"""

print(task)

print("origin   | rjust      | ljust     ")
for i in "123.456", "123.45", "23.45":
    print("{:8} | {:10} | {:10}".format(i, i.rjust(10, '0'), i.ljust(10, '0')))