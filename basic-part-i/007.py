#!/usr/bin/env python3

task = """
Task:
Write a Python program to accept a filename from the user and print the extension of that.
"""

print(task)

f_name = input("Enter filename: ")

f_split = f_name.split(".")

print("Extension:", repr(f_split[-1]))