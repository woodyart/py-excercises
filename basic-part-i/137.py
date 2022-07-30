#!/usr/bin/env python3

task = """
Task:
Write a Python program to extract single key-value pair of a dictionary in variables.
"""

print(task)

def dict_extract_single(number):
    return list(dict.items())[number]

dict = { "Hello" : "World", "Foo" : "Bar" }

x, y = dict_extract_single(1)

print("Dictionary:", dict)
print("X:", x, "Y: ", y)