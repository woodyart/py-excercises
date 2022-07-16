#!/usr/bin/env python3

import site

task = """
Task:
Write a Python program to locate Python site-packages.
"""

print(task)

print(','.join(site.getsitepackages()))
print(site.getusersitepackages())