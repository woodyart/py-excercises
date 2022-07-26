#!/usr/bin/env python3

task = """
Task:
Write a Python program to input a number, if it is not a number generates an error message.
"""

print(task)

while True:
    try:
        num = int(input("Enter number: "))
        print("Good! You entered a number!\n")
    except ValueError:
        print("Wrong!!! It's not a number!\n")