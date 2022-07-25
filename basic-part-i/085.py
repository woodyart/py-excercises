#!/usr/bin/env python3

from pathlib import Path

task = """
Task:
Write a Python program to check whether a file path is a file or a directory.
"""

print(task)

filepath = Path(input("Enter path: "))

if filepath.exists():
    if filepath.is_file():
        print("{} is file".format(filepath))
    elif filepath.is_dir():
        print("{} is directory".format(filepath))
    else:
        print("{} is nor directory or nor file but something else".format(filepath))