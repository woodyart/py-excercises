#!/usr/bin/env python3

from datetime import datetime
import time
task = """
Task:
Write a Python program to get the system time.

Note : The system time is important for debugging,
network information, random number seeds, or
something as simple as program performance.
"""

print(task)

print(datetime.now())
print(time.ctime())