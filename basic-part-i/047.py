#!/usr/bin/env python3

import os
import multiprocessing
import psutil

task = """
Task:
Write a Python program to find out the number of CPUs using.
"""

print("First try:", os.cpu_count())
print("Second try:", multiprocessing.cpu_count())
print("Third try (not working properly on MacOS):", psutil.cpu_count())