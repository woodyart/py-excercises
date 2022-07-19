#!/usr/bin/env python3

task = """
Task:
Write a Python program to calculate sum of digits of a number.
"""

print(task)

def sum_of_dig(num):
    sum = 0
    for n in str(num):
        sum += int(n)
    return sum

num = int(input("Enter number: "))
print("The sum of {} is {}".format(num, sum_of_dig(num)))