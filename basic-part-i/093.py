#!/usr/bin/env python3

task = """
Task:
Write a Python program to get the Identity, Type, and Value of an object.
"""

print(task)

print("{:10} | {:15} | {}".format('Identity'.center(10), 'Type'.center(15), 'Value'.center(10)))

a = "Hello World!"
b = 132
c = [5, 'abc', "def"]
d = (6, 'foo', "bar")

for i in a, b, c, d:
    print("{:>10} | {:<15} | {}".format(str(id(i)), str(type(i)), i))