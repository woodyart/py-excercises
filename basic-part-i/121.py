#!/usr/bin/env python3

task = """
Task:
Write a Python program to determine whether variable is defined or not.
"""

print(task)

x = 'abc'


try:
    x
    print("Variable is defined")
except NameError: print("Variable is not defined")

try:
    y
    print("Variable is defined")
except NameError: print("Variable is not defined")