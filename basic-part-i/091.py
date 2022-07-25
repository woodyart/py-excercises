#!/usr/bin/env python3

task = """
Task:
Write a Python program to swap two variables.
"""

print(task)

v1 = "one"
v2 = "two"

print("v1: {}, v2: {}".format(v1, v2))

v1, v2 = v2, v1

print("v1: {}, v2: {}".format(v1, v2))