#!/usr/bin/env python3


task = """
Task:
Write a Python program to get the difference between a given number and 17,
if the number is greater than 17 return double the absolute difference.
"""

print(task)

x = 17
y = int(input("Enter number: "))

if y < 17:
    dif = x - y
    print("The difference between 17 is", dif)
elif y == 17:
    print("Entered number is equal to 17")
else:
    dif = 2 * (y - x)
    print("Double absolute difference is", dif)