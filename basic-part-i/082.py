#!/usr/bin/env python3

task = """
Task:
Write a Python program to calculate the sum of all items of a container
(tuple, list, set, dictionary).
"""

print(task)

def sum_all_items(container):
    sum = 0
    for item in container:
        sum += item
    return sum

a = [1, 2, 3]
b = (1, 2, 3)
c = {1, 2, 3}

for item in a, b, c:
    print("Sum of", item, "=", sum_all_items(item))