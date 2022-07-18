#!/usr/bin/env python3

task = """
Task:
Write a Python program to convert height (in feet and inches) to centimeters.
"""

print(task)

def feet_to_cm(feet):
    return feet * 30.48

def inch_to_cm(inch):
    return inch * 2.54

src_feet = float(input("Enter feet value: "))
src_inch = float(input("Enter inch value: "))

cm = feet_to_cm(src_feet) + inch_to_cm(src_inch)

print("{}ft {}\" = {} cm".format(src_feet, src_inch, round(cm, 2)))