#!/usr/bin/env python3

from time import time

task = """
Task:
Write a Python program to get execution time for a Python method.
"""

print(task)

def test_method():
    start = time()
    v = 200**200
    finish = time() - start
    return finish


test_method()

print("Execution time: {} seconds".format(test_method()))