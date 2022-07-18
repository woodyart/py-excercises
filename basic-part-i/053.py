#!/usr/bin/env python3

import os

task = """
Task:
Write a python program to access environment variables.
"""

print(task)

for item in os.environ:
    print(item, ':' , os.environ[item])