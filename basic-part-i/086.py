#!/usr/bin/env python3

task = """
Task:
Write a Python program to get the ASCII value of a character.
"""

print(task)

my_char = input("Enter character: ")
print("""
Char | ASCII
{:>4} | {:>4}
""".format(my_char, ord(my_char)))