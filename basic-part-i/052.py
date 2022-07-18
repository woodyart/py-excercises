#!/usr/bin/env python3

from pathlib import Path
import logging

task = """
Task:
Write a Python program to print to stderr.
"""

print(task)

print("""To check only stderr messages run script with command:
./{} 2>&1 > /dev/null
""".format(Path(__file__).name))

fmt = '%(message)s'
logging.basicConfig(format=fmt)
logging.warning("Stderr message!")