#!/usr/bin/env python3

import os
import time

task = """
Task:
Write a Python program to sort files by date.
"""

print(task)

def sortfiles(workdir):
    os.chdir(workdir)
    files = filter(os.path.isfile, os.listdir(workdir))
    files = [os.path.join(workdir, f) for f in files]
    return sorted(files, key=lambda x: os.path.getmtime(x))


for item in sortfiles('.'):
    print(item, time.ctime(os.path.getmtime(item)))