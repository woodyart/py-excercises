#!/usr/bin/env python3

task = """
Task:
Write a Python program to print Unicode characters.
"""

print(task)

unicode = "\u00af\_(\u30c4)_/\u00af"
print(unicode, '==', ascii(unicode))