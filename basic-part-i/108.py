#!/usr/bin/env python3

from pathlib import Path

task = """
Task:
Write a Python program to find path refers to a file or directory when you encounter a path name.
"""

print(task)

f = Path(__file__)

print("""
File         : {}
is Absolute  : {}
Is Exist     : {}
Is File      : {}
Is Directory : {}
is Symlink   : {}
""".format(f, f.is_absolute(), f.exists(), f.is_file(), f.is_dir(), f.is_symlink()))