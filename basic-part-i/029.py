#!/usr/bin/env python3

task = """
Task:
Write a Python program to print out a set containing all the colors
from color_list_1 which are not present in color_list_2.
"""

print(task)

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

color_set_uniq = color_list_1.difference(color_list_2)

print("Color Set 1:", color_list_1)
print("Color Set 2:", color_list_2)
print("Unique colors:", color_set_uniq)