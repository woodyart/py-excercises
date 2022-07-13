#!/usr/bin/env python3

from datetime import date

task = """
Task:
Write a Python program to display the examination schedule. (extract the date from exam_st_date).
"""

print(task)

exam_st_date = (11, 12, 2014)

print("exam_st_date =", exam_st_date)

print("\nFirst try - Convert exam_st_date into date object")

exam_date = date(exam_st_date[2], exam_st_date[1], exam_st_date[0])

print("The examination schedult will start from:", exam_date.strftime("%d / %m / %Y"))

print("\nSecond try - Format exam_st_date string")
print("The examination schedult will start from: %i / %i / %i" % exam_st_date)