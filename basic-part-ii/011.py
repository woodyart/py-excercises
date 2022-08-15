#!/usr/bin/env python3


import itertools

task = """
Task:
Write a Python program to check the sum of three elements (each from an array) from three arrays is equal to a target value.
Print all those three-element combinations.
"""

print(task)

x = [10, 20, 20, 20]
y = [10, 20, 30, 40]
z = [10, 30, 40, 20]
target = 70

# Easy one
print("First try:")
for xi, xk in enumerate(x):
    for yi, yk in enumerate(y):
        for zi, zk in enumerate(z):
            if xk + yk + zk == target:
                print("x[{}] + y[{}] + z[{}] = {} + {} + {} = {}".format(xi, yi, zi, xk, yk, zk, target))

# More interesting
print("\nSecond try:")
combs = itertools.product(x,y,z)
for i in combs:
    if sum(i) == target:
        print(i)