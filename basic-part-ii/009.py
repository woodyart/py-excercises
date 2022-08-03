#!/usr/bin/env python3

import pkg_resources

task = """
Task:
Write a Python program to get a list of locally installed Python modules.
"""

print(task)

[print(i.key, '=', i.version) for i in pkg_resources.working_set]