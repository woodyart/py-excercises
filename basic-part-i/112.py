#!/usr/bin/env python3

task = """
Task:
Write a Python program to remove the first item from a specified list.
"""

print(task)

lst = ['one', 'two', 'three']
print("Before  :", lst)

lst.remove(lst[0])
print("After(1):", lst)

del lst[0]
print("After(2):", lst)