#!/usr/bin/env python3

from datetime import date
from datetime import timedelta

task = """
Task:
Write a Python program to calculate number of days between two dates.
"""

print(task)

date1_str = input("Enter first date: ").split('.')
date1 = date(int(date1_str[0]), int(date1_str[1]), int(date1_str[2]))

date2_str = input("Enter second date: ").split('.')
date2 = date(int(date2_str[0]), int(date2_str[1]), int(date2_str[2]))

days = date1 - date2
print("Days between:", days.days)