#!/usr/bin/env python3

task = """
Task:
Write a Python program to create a bytearray from a list.
"""

print(task)

lst = [10, 2, 3, 100]
b_lst = bytearray(lst)

print(lst, '==', b_lst)

for i in b_lst: print(i)