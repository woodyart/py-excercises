#!/usr/bin/env python3

from inspect import getmodule
from http import client

task = """
Task:
Write a Python program to get the actual module object for a given object.
"""

print(task)

c = client.HTTPConnection("http://example.com/", 80)

print(getmodule(c))