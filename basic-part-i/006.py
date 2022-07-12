#!/usr/bin/env python3

task = """
Task:
Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. 
"""

print(task)

a_seq = input("Enter number sequence: ")

a_list = a_seq.split(",")
a_tuple = tuple(a_list)

print("LIST:",a_list, "\nTUPLE:", a_tuple)