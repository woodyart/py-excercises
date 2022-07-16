#!/usr/bin/env python3

import platform

task = """
Task:
Write a Python program to get OS name, platform and release information.
"""

print(task)

os_name     = platform.system()
os_release  = platform.release()
os_platform = platform.platform()

print("""
OS name  : {}
Release  : {}
Platform : {}
""".format(os_name, os_release, os_platform))