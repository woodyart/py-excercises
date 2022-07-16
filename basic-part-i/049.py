#!/usr/bin/env python3

from pathlib import Path

task = """
Task:
Write a Python program to list all files in a directory in Python.
"""

print(task)

workdir = Path('.')

list_files = [f for f in workdir.iterdir() if f.is_file()]

print(workdir.absolute(), ":")
for f in sorted(list_files): print(f.name)