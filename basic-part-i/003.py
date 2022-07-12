#!/usr/bin/env python3

from datetime import datetime

task = """
Task:
Write a Python program to display the current date and time.
"""

print(task)

d = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("Current date and time:\n" + d)