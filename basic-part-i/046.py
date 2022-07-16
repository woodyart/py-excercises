#!/usr/bin/env python3

from pathlib import Path

task = """
Task:
Write a python program to get the path and name of the file that is currently executing.
"""

print(task)

prog_path = Path(__file__).absolute()
prog_name = Path(__file__).name

print("""Currently executing script info
Name: {}
Path: {}
""".format(prog_name, prog_path))