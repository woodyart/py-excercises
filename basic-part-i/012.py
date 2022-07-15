#!/usr/bin/env python3

from datetime import date
import calendar

task = """
Task:
Write a Python program to print the calendar of a given month and year.
"""

print(task)

now = date.today()
cal = calendar.month(now.year, now.month)

print(cal)