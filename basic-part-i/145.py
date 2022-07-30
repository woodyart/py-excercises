#!/usr/bin/env python3

task = """
Task:
Write a Python program to test if a variable is a list or tuple or a set.
"""

print(task)

for i in (1, 2, 3), [4, 5, 6], {7, 8, 9}, {1:2, 3:4}, 123, 'foo':
    #'isinstance(x, foo)' and 'type(x) is foo' are equal
    if isinstance(i, list) or type(i) is list:
        print(i, 'is list')
    elif isinstance(i, tuple) or type(i) is tuple:
        print(i, 'is tuple')
    elif isinstance(i, set) or type(i) is set:
        print(i, 'is set')
    else: print(i, 'is not list nor tuple nor set')