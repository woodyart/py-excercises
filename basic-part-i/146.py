#!/usr/bin/env python3

from pathlib import Path
import imp
import math
import pandas
import ipaddress

task = """
Task:
Write a Python program to find the location of Python module sources.
"""

print(task)

print("First try:")
print(Path(math.__file__).parents[0])
print(Path(pandas.__file__).parents[0])
print(Path(ipaddress.__file__).parents[0])
print("")

print("Second try:")
print(imp.find_module('math')[1])
print(imp.find_module('pandas')[1])
print(imp.find_module('ipaddress')[1])