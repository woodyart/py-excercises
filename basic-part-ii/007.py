#!/usr/bin/env python3

from collections import Counter

task = """
Task:
Write a Python program to count the number of each character of a given text of a text file.
"""

print(task)

file = '007.txt'

def count_chars(file):
    char_count = Counter()
    f = open(file, 'r')
    while True:
        line = f.readline()
        if not line:
            break
        c = list(line.replace('\n',''))
        c = dict(Counter(c))
        char_count.update(c)
    f.close()
    return dict(char_count)


c = count_chars(file)

for key, val in c.items():
    print('{}:{:3}'.format(key,  val))