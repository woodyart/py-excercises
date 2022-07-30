#!/usr/bin/env python3

task = """
Task:
Write a Python function to check whether a distinct pair of numbers
whose product is odd present in a sequence of integer values.
"""

print(task)

def check_odd_pair(seq):
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if seq[i]*seq[j] %2 == 1: return True
    return False

a = [ 8, 2, 4, 6, 3, 7 ]
b = [ 2, 4, 6 ]
c = [ 3, 3 ]

for i in a, b, c: print(i, check_odd_pair(i))