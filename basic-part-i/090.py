#!/usr/bin/env python3

import shutil

task = """
Task:
Write a Python program to create a copy of its own source code.
"""

print(task)

shutil.copy(__file__, __file__+'-copy')