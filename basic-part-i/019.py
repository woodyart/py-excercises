#!/usr/bin/env python3

import re

task = """
Task:
Write a Python program to get a new string from a given string where "Is" has been added to the front.
If the given string already begins with "Is" then return the string unchanged. 
"""

print(task)


def is_apply(str):
    pattern = re.compile(r'^Is')
    match = re.search(pattern, str)
    if match:
        return str
    else:
        str = "Is" + str
        return str

strings = ["Is this a code?", "Yes. It is", "Ok. Is it work?"]

for s in strings:
    print(is_apply(s))