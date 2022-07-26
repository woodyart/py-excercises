#!/usr/bin/env python3

task = """
Task:
Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.
"""

print(task)

numbers = (0, 15, 30 ,31 ,20, 45, 99, 90)

divisible = list(filter(lambda x: (x%15 == 0) , numbers))

print("Source list     :", numbers)
print("Divisible by 15 :", divisible)