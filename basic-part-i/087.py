#!/usr/bin/env python3

from pathlib import Path
import os

task = """
Task:
Write a Python program to get the size of a file.
"""

print(task)

print("""
File: {}
Size: {} bytes (First try)
Size: {} bytes (Second try)
""".format( 
    Path(__file__).name, 
    Path(__file__).stat().st_size, 
    os.path.getsize(__file__)
    ))