#!/usr/bin/env python3

task = """
Task:
Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
"""

print(task)

user = input("Enter your first and last name: ")

user_list = user.split()
user_list.reverse()

print("Hello,", *user_list)