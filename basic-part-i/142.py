#!/usr/bin/env python3

task = """
Task:
Write a Python program to check if every consecutive sequence of zeroes is followed by
a consecutive sequence of ones of same length in a given string. Return True/False.
"""

print(task)

def seq_check(seq):
    while '01' in seq:
        seq = seq.replace('01', '')
    return len(seq) == 0

seq = ["01010101", "00", "000111000111", "00011100011"]

for i in seq: print( "{:12} - {}".format( i, seq_check(i) ) )