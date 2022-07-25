#!/usr/bin/env python3

import sys

task = """
Task:
Write a Python program to find the available built-in modules.
"""

print( *sys.builtin_module_names, sep='\n' )