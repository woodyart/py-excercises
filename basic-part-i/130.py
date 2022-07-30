#!/usr/bin/env python3

task = """
Task:
Write a Python program to use double quotes to display strings.
"""

print(task)

s = "Hello world"

print('"' + s + '"')
print("\"{}\"".format(s))