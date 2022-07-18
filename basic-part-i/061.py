#!/usr/bin/env python3

task = """
Task:
Write a Python program to convert the distance (in feet) to inches, yards, and miles.
"""

print(task)

def ft_to_inches(n):
  return n * 12

def ft_to_yards(n):
  return n / 3

def ft_to_miles(n):
  return n / 5280

distance = float(input("Enter distance, ft: "))

print("{} ft = {}\" or {} yd or {} mi".format(distance, ft_to_inches(distance), ft_to_yards(distance), ft_to_miles(distance)))