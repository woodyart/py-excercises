#!/usr/bin/env python3

from struct import calcsize

task = """
Task:
Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system.
"""

print(task)

mode = calcsize("P") * 8

print("Python shell is executing in {}bit mode".format(mode))