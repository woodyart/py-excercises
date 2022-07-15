#!/usr/bin/env python3

task = """
Task:
Write a Python program to calculate the sum of three given numbers,
if the values are equal then return three times of their sum.
"""

print(task)

def check_same(list):
    for item in list:
        if item != list[0]:
            return False
    return True

def result(list):
    if check_same(list) is True:
        return(sum(list) * 3)
    else:
        return(sum(list))
        

x = [7, 5, 2]
y = [5, 5, 5]

for item in x, y:
    print(item, result(item))