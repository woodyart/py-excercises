#!/usr/bin/env python3

task = """
Task:
Write a Python program that will accept the base and height of a triangle and compute the area.
"""

print(task)

tr_base = int(input("Enter base: "))
tr_height = int(input("Enter height: "))

tr_area = tr_base * tr_height / 2

print("Triangle area:", tr_area)