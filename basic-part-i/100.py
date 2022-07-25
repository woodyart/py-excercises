#!/usr/bin/env python3

from os import uname
from socket import gethostname
from platform import node

task = """
Task:
Write a Python program to get the name of the host on which the routine is running.
"""

print(task)

print("First try  :", uname().nodename)
print("Second try :", gethostname())
print("Third try  :", node())