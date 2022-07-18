#!/usr/bin/env python3

import profile

task = """
Task:
Write a Python program to determine profiling of Python programs.
"""

print(task)

w = """
HeLlO0 WoRLd!1!!1 HeLlO0 WoRLd!1!!1 HeLlO0 WoRLd!1!!1 HeLlO0 WoRLd!1!!1
HeLlO0 WoRLd!1!!1 HeLlO0 WoRLd!1!!1 HeLlO0 WoRLd!1!!1 HeLlO0 WoRLd!1!!1
HeLlO0 WoRLd!1!!1 HeLlO0 WoRLd!1!!1 HeLlO0 WoRLd!1!!1 HeLlO0 WoRLd!1!!1
HeLlO0 WoRLd!1!!1 HeLlO0 WoRLd!1!!1 HeLlO0 WoRLd!1!!1 HeLlO0 WoRLd!1!!1
"""

profile.run('print(w)')
profile.run('print(w.lower())')
profile.run('print(w.casefold())')