#!/usr/bin/env python3

from itertools import combinations

task = """
Task:
Write a Python program to get all possible two digit letter combinations from a digit (1 to 9) string.
"""

print(task)

string_maps = {
"1": "abc",
"2": "def",
"3": "ghi",
"4": "jkl",
"5": "mno",
"6": "pqrs",
"7": "tuv",
"8": "wxy",
"9": "z"
}

def get_all_combs_of_2(num):
    n1 = str(num)[0]
    n2 = str(num)[1]
    word = string_maps.get(n1) + string_maps.get(n2)
    for i in list(combinations(word, 2)):
        print(''.join(i))

print("---------47:")
get_all_combs_of_2(47)

print("---------29:")
get_all_combs_of_2(29)