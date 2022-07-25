#!/usr/bin/env python3

import sys

task = """
Task:
Write a Python program to get the command-line arguments 
(name of the script, the number of arguments, arguments) passed to a script.
"""

print(task)

print("""
Script name     : {}
Passed args num : {}
Passed args     : {}
""".format(sys.argv[0], len(sys.argv[1:]), sys.argv[1:]))