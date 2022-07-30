#!/usr/bin/env python3

import collections

task = """
Task:
Write a Python program to sum of all counts in a collections.
"""

print(task)

c = (5, 5, 5, 2, 3, 1, 1, 1, 1, 1)
c_sum = sum(collections.Counter(c).values())

# When python --version >= 3.10
#c_sum = collections.Counter(c).total()

print(c)
print(c_sum)
