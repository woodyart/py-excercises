#!/usr/bin/env python3

task = """
Task:
Write a Python program to add two positive integers without using the '+' operator.
Note: Use bit wise operations to add two numbers.
"""

print(task)

def bitwise_sum(a, b):
    tmp = (a & b) << 1
    sum = a ^ b

    if tmp == 0:
        return sum

    return  bitwise_sum(tmp, sum)


a1 = 25
a2 = 5
print("Sum of {} and {} is {}".format(a1, a2, bitwise_sum(a1, a2)))