#!/usr/bin/env python3

task = """
Task:
Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
"""

print(task)

f = input("Enter function name: ")

help(f)