#!/usr/bin/env python3

import os
import getpass

task = """
Task:
Write a Python program to get the current username.
"""

print(task)

print("First try. Current username is", os.environ['USER'])
print("Second try. Current username is", getpass.getuser())