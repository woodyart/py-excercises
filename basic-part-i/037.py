#!/usr/bin/env python3

task = """
Task:
Write a Python program to display your details like name, age, address in three different lines.
"""

print(task)

def student_info(name, age, address):
    print("""
Name:    {}
Age :    {}
Address: {}
""".format(name, age, address) )

s = ["Andrey", "1900", "Nowhere 153"]

student_info(s[0], s[1], s[2])