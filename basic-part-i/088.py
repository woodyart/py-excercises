#!/usr/bin/env python3

from pathlib import Path
import os

task = """
Task:
Given variables x=30 and y=20, write a Python program to print "30+20=50".
"""

print(task)

x = 30
y = 20

print("{}+{}={}".format(x, y, x+y))