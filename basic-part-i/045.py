#!/usr/bin/env python3

from subprocess import run

task = """
Task:
Write a Python program to call an external command.
"""

print(task)

run(["ls", "-1"])