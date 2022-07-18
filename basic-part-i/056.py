#!/usr/bin/env python3

import os

task = """
Task:
Write a Python program to get height and width of the console window.
"""

print(task)

columns, lines = os.get_terminal_size()

print("Terminal size: {}x{} (lines x Columns)".format(lines, columns))