#!/usr/bin/env python3

import sys

task = """
Task:
Write a Python program to get the size of an object in bytes.
"""

print(task)

a = 1
b = '1'
c = ('1')
d = ['1']
e = { '1' : '1' }
f = [1]
g = [1.0]

print("{:15} | {:12} | {}".format('---------------', '------------', '------------'))
print("{:15} | {:12} | {}".format('Object Type', 'Size (bytes)', 'Value'))
print("{:15} | {:12} | {}".format('---------------', '------------', '------------'))
for item in a, b, c, d, e, f, g :
    print("{:<15} | {:>12} | {}".format(str(type(item)), sys.getsizeof(item), item))