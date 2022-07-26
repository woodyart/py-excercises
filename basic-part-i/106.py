#!/usr/bin/env python3

from pathlib import Path

task = """
Task:
Write a Python program to divide a path on the extension separator.
"""

print(task)

for file in __file__, '/', '/tmp/hello.txt', '', 'world.zip':
    file = Path(file)
    print("File '{}' has '{}' extension".format(file, file.suffix))