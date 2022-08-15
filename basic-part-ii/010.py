#!/usr/bin/env python3

import platform

task = """
Task:
Write a Python program to display some information about the OS where the script is running.
"""

os = platform.platform()
system = platform.uname().system
release = platform.uname().release
machine = platform.uname().machine

print("""
-======OS Info======-
OS       : {}
Platform : {} {} {}
""".format(os, system, release, machine))