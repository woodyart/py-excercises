#!/usr/bin/env python3

task = """
Task:
Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.
"""

print(task)

def clear_list_every(lst, num):
    start = 0
    jump = num - 1

    while len(lst) > 0:
        start += jump
        if start > len(lst): start = start % len(lst)
        print(lst[start])
        lst.remove(lst[start])


a = [ 10, 20, 30, 40, 50, 60, 70, 80, 90]

print(a)
clear_list_every(a, 3)
