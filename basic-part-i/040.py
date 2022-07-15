#!/usr/bin/env python3

from math import sqrt


task = """
Task:
Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
"""

print(task)

def get_distance(x1, y1, x2, y2):
    # d = √[(x2− x1)^2 + (y2−y1)^2]
    d = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return d

x1 = 0
y1 = 0

x2 = 10
y2 = 10

distance = round(get_distance(x1,y1, x2,y2), 2)

print("Distance between ({};{}) and ({};{}) is {}".format(x1,y1, x2,y2, distance))