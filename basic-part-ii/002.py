#!/usr/bin/env python3

task = """
Task:
Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'.
Use the characters exactly once.
"""

print(task)

def iter_combinations(s):
    combinations = []
    for _ in range(len(s)):
        a = s[-1]
        s.remove(a)
        s.insert(0, a)
        combinations.append(''.join(s))
    return sorted(combinations)

a = [ 'a', 'e', 'i', 'o', 'u' ]

print(iter_combinations(a))