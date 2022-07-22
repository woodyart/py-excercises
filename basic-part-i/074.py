#!/usr/bin/env python3

task = """
Task:
Write a Python program to hash a word.
"""

print(task)

word = input("Enter word: ")
print("Word: {}. Hash: {}".format(word, hash(word)))