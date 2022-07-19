#!/usr/bin/env python3

from datetime import timedelta

task = """
Task:
Write a Python program to convert seconds to day, hour, minutes and seconds.
"""

print(task)

s = int(input("Enter seconds: "))

s_date = timedelta(seconds=s)

print("{} seconds = {} ".format(s, timedelta(seconds=s)))