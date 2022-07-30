#!/usr/bin/env python3

from datetime import datetime
from time import sleep
from timeit import default_timer

task = """
Task:
Write a Python program to calculate the time runs (difference between start and current time) of a program.
"""

print(task)

def dt_check(seconds):
    start = datetime.timestamp(datetime.now())
    print("Datetime - sleep {} seconds".format(seconds))
    sleep(seconds)
    return datetime.timestamp(datetime.now()) - start

def t_check(seconds):
    start = default_timer()
    print("Timeit   - sleep {} seconds".format(seconds))
    sleep(seconds)
    return default_timer() - start

s = 2

print("""
Check with datetime : {} seconds
Check with timeit   : {} seconds
""".format(dt_check(s), t_check(s)))