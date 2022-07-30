#!/usr/bin/env python3

import sys

task = """
Task:
Write a Python program to determine the largest and smallest integers, longs, floats.
"""

print(task)

print("Float info: max -", sys.float_info.max, "min -", sys.float_info.min)
print("Int info", sys.int_info)
print("Int max -", sys.maxsize)