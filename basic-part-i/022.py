#!/usr/bin/env python3

task = """
Task:
Write a Python program to count the number 4 in a given list.
"""

print(task)

a = [1, 2, 3, 4, 4, 5, 6, 7, 4, 44 ]

c = a.count(4)

print("List:", a)
print("The '4' number appears in the list", c, "time(s)")