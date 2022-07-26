#!/usr/bin/env python3

from functools import reduce
from numpy import product


task = """
Task:
Write a Python program to compute the product of a list of integers
(without using for loop).
"""

print(task)

all_nums = (1, -1, 2, 3, -5, 4)
p = product(all_nums)

print('Product of', all_nums, '=', p, '(numpy)')
print('Product of', all_nums, '=', reduce(lambda x, y: x * y, all_nums), '(functools)')