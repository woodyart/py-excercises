#!/usr/bin/env python3

task = """
Task:
Write a Python program to round a floating-point number to specified number decimal places.
"""

print(task)

f = 123.456

print("""Static round:
{}
{:.2f}
{:.5f}
""".format(f, f, f))

i = int(input("Specify decimal places for {}: ".format(f)))
print(round(f, i))