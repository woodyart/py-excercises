#!/usr/bin/env python3

task = """
Task:
Write a Python program to find the number of zeros at the end of a factorial of a given positive number.
Range of the number(n): (1 <= n <= 2*109).
"""

print(task)

def count_trailing_zeroes(n):
    counter = 0
    for i in list(reversed(str(n))):
        if int(i) != 0:
            return counter
        else:
            counter += 1

def get_factorial_last_zeroes(n):
    from math import factorial
    f = factorial(n)
    return count_trailing_zeroes(f)

for i in range(0, 100+1, 10):
    print("Number of zeroes at the end of {}! is {}".format(i, get_factorial_last_zeroes(i)))