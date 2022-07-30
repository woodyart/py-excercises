#!/usr/bin/env python3

task = """
Task:
Write a Python function that takes a positive integer
and returns the sum of the cube of all the positive integers
smaller than the specified number.
"""

print(task)

def all_sum_cube(n):
    n -= 1
    sum = 0
    while n > 0:
        sum += n ** 3
        n -= 1
    return sum

for i in range(3, 7):
    print("Sum of cubes for {} = {}".format(i, all_sum_cube(i)))