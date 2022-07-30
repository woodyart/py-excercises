#!/usr/bin/env python3

from pathlib import Path

task = """
Task:
Write a Python program to find files and skip directories of a given directory.
"""

print(task)

dir = input("Enter directory path: ")

print( *list( filter( lambda x: x.is_file(), Path(dir).iterdir() ) ), sep='\n' )