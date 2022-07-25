#!/usr/bin/env python3

task = """
Task:
Write a Python program to perform an action if a condition is true.
Given a variable name, if the value is 1, display the string "First day of a Month!" 
and do nothing if the value is not equal.
"""

print(task)

message = "First day of a Month!"

v = input("Enter value: ")

if v == '1':
    print(message)