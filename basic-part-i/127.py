#!/usr/bin/env python3

task = """
Task:
Write a Python program to check whether an integer fits in 64 bits.
"""

print(task)

a = 1
b = 2 ** 31
c = 2 ** 63
d = 2 ** 64 - 1
e = 2 ** 64

print("{:20} | {:7} | {}".format('Value', 'Bitness', 'Fit 64'))
for i in a, b, c, d, e: print("{:20} | {:3} bit | {}".format(i, i.bit_length(), i.bit_length() <= 64))