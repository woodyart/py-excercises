#!/usr/bin/env python3

from glob import glob

task = """
Task:
Write a Python program to make file lists from current directory using a wildcard.
"""

print(task)

wildcard = '05*.py'
print("wildcard : ", wildcard)
print("files    : ", sorted(glob(wildcard)))