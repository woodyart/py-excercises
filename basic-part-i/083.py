#!/usr/bin/env python3

task = """
Task:
Write a Python program to test whether all numbers of a list is greater than a certain number.
"""

print(task)

def test_greater(l, n):
    return all(item > n for item in l)

n = 4

l1 = (1, 2, 3, 4, 5, 6, 7, 8)
l2 = (5, 6, 7, 8, 9, 9, 9, 9)

for l in l1, l2:
    print(l, "is greater than", n, ':', test_greater(l, n))