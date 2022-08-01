#!/usr/bin/env python3

task = """
Task:
Write a Python program to find unique triplets whose three elements gives the sum of zero from an array of n integers.
"""

print(task)

def if_out_of_range(val, num):
    if val < num: return val
    elif val == num: return 0
    elif val == num+1: return 1 


def find_zero_triplets(lst):
    if len(lst) < 3:
        print("Can't find triplets - given list too short", lst)
        return False
    for x in range(0, len(lst)):
        n1 = x
        n2 = if_out_of_range(x+1, len(lst))
        n3 = if_out_of_range(x+2, len(lst))
        
        if lst[n1] + lst[n2] + lst[n3] == 0:
            print("{} + {} + {} = 0".format(lst[n1], lst[n2], lst[n3]))


a = [ 10, -6, 4, 2, 20, 30, 40, 50, 60, 70, 80, 90]
b = [ 1, -1 ]
c = [1, -6, 4, 2, -1, 2, 0, -2, 0 ]

for i in a, b, c:
    print(i)
    find_zero_triplets(i)
