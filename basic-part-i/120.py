#!/usr/bin/env python3

task = """
Task:
Write a Python program to format a specified string limiting the length of a string.
"""

print(task)

s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

print("""
Original string: {}
Length: {} characters
""".format(s, len(s)))

print("""
Shorten string: {:.5}
Length: {} characters
""".format(s, len(s)))

lim = int(input("Enter limit size: "))

print("""
Shrinked string: {}
Length: {} characters
""".format(s[:lim], len(s)))