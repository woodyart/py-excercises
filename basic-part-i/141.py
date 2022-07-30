#!/usr/bin/env python3

task = """
Task:
Write a python program to convert decimal to hexadecimal.
"""

print(task)

x = int(input("Enter value: "))
print( '{} = {:02x}'.format(x, x) )