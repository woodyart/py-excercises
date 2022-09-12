#!/usr/bin/env python3

task = """
Task:
Write a Python program to find the value of n where n degrees of number 2 are written sequentially in a line without spaces.
"""

print(task)

def count_degree_of_2(d):
    n = 0
    while str( pow(2, n+1) ) in d:
        n += 1
    return n

dataset = ["248", "12481632", "248163264128", "111"]

for data in dataset:
    print("Count degrees of 2 in {}: {}".format(data, count_degree_of_2(data)))