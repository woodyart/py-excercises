#!/usr/bin/env python3

task = """
Task:
Write a Python program to concatenate N strings.
"""

print(task)

strings = ["one", "two", "three", "four"]

print("Strings:", strings)

print("\nConcatenation (First try):")
print(''.join(strings))

print("\nConcatenation (Second try):")
print(*strings, sep='')