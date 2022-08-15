#!/usr/bin/env python3

from itertools import permutations

task = """
Task:
Write a Python program to create all possible permutations from a given collection of distinct numbers.
"""

print(task)

a = [1, 2, 3]

print(list(permutations(a)))