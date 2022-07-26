#!/usr/bin/env python3

task = """
Task:
Write a Python program to prove that two string variables 
of same value point same memory location.
"""

print(task)

a = "hello"
b = "world"
c = "hello"

for item in a, b, c:
    print(item, "point to", hex(id(item)))