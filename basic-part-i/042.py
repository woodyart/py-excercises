#!/usr/bin/env python3

import platform

task = """
Task:
Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS. 
"""

print(task)

print("OS mode is", platform.architecture()[0])