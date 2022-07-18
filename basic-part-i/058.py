#!/usr/bin/env python3

task = """
Task:
Write a Python program to sum of the first n positive integers.
"""

print(task)

def sum_positive_n(n):
    sum = 0
    while n > 0:
        sum += n
        n -= 1
    return sum

def sum_positive_alt(n):
    return int((n * (n+1))/2)

n = int(input("Enter N: "))
print("First try:", sum_positive_n(n))
print("Second try:", sum_positive_alt(n))