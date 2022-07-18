#!/usr/bin/env python3

task = """
Task:
Write a Python program to get an absolute file path.
"""

print(task)

def get_absolute(f_name):
  from pathlib import Path
  return Path(f_name).absolute()

f = __file__

print("The absolute path of running script is {}".format(get_absolute(f)))