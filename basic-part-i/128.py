#!/usr/bin/env python3

task = """
Task:
Write a Python program to check whether lowercase letters exist in a string.
"""

print(task)

def count_lower(s):
    counter = 0
    for i in s:
        if i.islower(): counter += 1
    return counter

def any_lower(s):
    return any(i.islower() for i in s)

s_low = "alllower"
s_upp = "ALLUPPER"
s_mix = "All MiXeD"

for i in s_low, s_upp, s_mix:
    print("String '{}' has lowercase letters: {} ({})".format(i, any_lower(i), count_lower(i)))