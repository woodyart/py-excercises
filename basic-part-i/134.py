#!/usr/bin/env python3

task = """
Task:
Write a Python program to input two integers in a single line.
"""

print(task)

a = [ int(x) for x in input("Enter two numbers: ").split() ]

for i in a: print(i)

x, y = map(int, input("Enter two numbers: ").split())
print("{}\r\n{}".format(x, y))