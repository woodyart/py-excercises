#!/usr/bin/env python3

task = """
Task:
Write a Python program to filter the positive numbers from a list.
"""

print(task)

all_nums = (1, -1, 2, 3, -5, 4)
pos_nums = list(filter(lambda x: (x >= 0) , all_nums))

print("All numbers    :", all_nums)
print("Positives only :", pos_nums)