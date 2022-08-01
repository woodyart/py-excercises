#!/usr/bin/env python3

from collections import Counter

task = """
Task:
Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies.
"""

print(task)

long_text = "Write a Python program to print a long text convert the string to a list and print all the words and their frequencies"

lst = str(long_text.lower()).split()

c = dict(Counter(lst))

print(long_text)
print(c)
for key, val in c.items():
    print('{:14}:{:3}'.format(key,  val))