#!/usr/bin/env python3

task = """
Task:
Write a Python program to calculate midpoints of a line.
"""

print(task)

def calc_line_midpoints(begin, end):
    return (begin[0] + end[0])/2, (begin[1] + end[1])/2

p_start = [1, 1]
p_end = [5, 3]

print("The midpoint of {} and {} is {}".format(p_start, p_end, calc_line_midpoints(p_start, p_end)))