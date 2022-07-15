#!/usr/bin/env python3

task = """
Task:
Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
Return the n copies of the whole string if the length is less than 2.
"""

print(task)

def copycut(str, num):
    if len(str) < 2:
        print( str * num )
    else:
        print( str[:2] * num )

strings = [ "Hello!",
            "Is",
            "this",
            "a",
            "good",
            "code?"
          ]

n = int(input("Enter number of copies: "))

for s in strings:
    print(s)
    copycut(s, n)