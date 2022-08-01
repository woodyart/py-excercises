#!/usr/bin/env python3

task = """
Task:
Write a Python function that takes a sequence of numbers
and determines whether all the numbers are different from each other.
"""

print(task)

def check_uniq_1(seq):
    for i in range(len(seq)):
        if seq.count(seq[i]) > 1: return False
    return True

def check_uniq_2(seq):
    if len(seq) == len(set(seq)): return True
    return False

a = [1, 2, 3]
b = [1, 1, 2]
c = [1, 2, 1]

for item in a, b, c:
    print(item, 'has uniq numbers:', check_uniq_1(item), check_uniq_2(item) )