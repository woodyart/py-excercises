#!/usr/bin/env python3

task = """
Task:
Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
"""

print(task)

a = [ 1, 2, 3, 4, 9, 8, 7, 6, 5, -100 ]

print("""
Source  : {}
Minimum : {}
Maximum : {}
""".format(a, min(a), max(a)))