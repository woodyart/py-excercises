#!/usr/bin/env python3

import os
from pathlib import Path

task = """
Task:
Write a Python program to list home directory without absolute path.
"""

print(task)

print('')
print(os.listdir(os.getenv("HOME")))
print('')
print(os.listdir(os.path.expanduser("~")))
print('')
print(list(Path.home().iterdir()))