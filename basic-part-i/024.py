#!/usr/bin/env python3

task = """
Task:
Write a Python program to test whether a passed letter is a vowel or not.
"""

print(task)

def isvowel(c):
    vowels = "aeiou"
    return c in vowels

l = input("Enter a letter: ")

if isvowel(l):
    print(l, "is a vowel")
else:
    print(l, "is a consonant")