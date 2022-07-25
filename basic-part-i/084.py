#!/usr/bin/env python3

task = """
Task:
Write a Python program to count the number occurrence of a specific character in a string.
"""

print(task)

my_string = str(input("Enter string: "))
my_char   = str(input("Enter character: "))

print("""
String    : {}
Character : {}
Count     : {}
""".format(my_string, my_char, my_string.count(my_char)))