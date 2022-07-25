#!/usr/bin/env python3

import sys

task = """
Task: Write a Python program to test whether the system 
is a big-endian platform or little-endian platform.
"""

print(task)

print("The system is a " + sys.byteorder.capitalize() + "-endian platform")