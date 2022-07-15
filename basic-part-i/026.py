#!/usr/bin/env python3

task = """
Task:
Write a Python program to concatenate all elements in a list into a string and return it.
"""

print(task)

def histogram(list):
    hist = {}
    for item in list:
        l = "*" * item
        hist[l] = item
    return hist

a = [1, 9, 2, 8, 3, 7, 4, 6, 5, 15, 16, 17]
h = histogram(a)

for k, v in h.items():
    print(f'{v:3} : {k}')