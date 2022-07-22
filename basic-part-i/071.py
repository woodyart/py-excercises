#!/usr/bin/env python3

import os
import time

task = """
Task:
Write a Python program to get a directory listing, sorted by creation date.
"""

print(task)

def sortfiles(workdir):
    os.chdir(workdir)
    files = filter(os.path.isfile, os.listdir(workdir))
    files = [os.path.join(workdir, f) for f in files]
    return sorted(files, key=lambda x: os.path.getctime(x))


for item in sortfiles('.'):
    print(time.ctime(os.path.getctime(item)), item)