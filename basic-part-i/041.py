#!/usr/bin/env python3

from pathlib import Path

task = """
Task:
Write a Python program to check whether a file exists.
"""

print(task)

def check_exist(p):
    if p.exists():
        if p.is_file():
            print(p, "- file exists :)")
        else:
            print(p, " exists, but it's a directory :(")
    else:
        print(p, "- file does not exist :(")

filename1 = Path('041.py')
filename2 = Path('xxx.py')
filename3 = Path('..')

check_exist(filename1)
check_exist(filename2)
check_exist(filename3)