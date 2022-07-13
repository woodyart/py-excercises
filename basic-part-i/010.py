#!/usr/bin/env python3

task = """
Task:
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
"""

print(task)

n = input("Enter value: ")
nn = n + n
nnn = nn + n

value = int(n) + int(nn) + int(nnn)
print("First try")
print("Result:", value)

x   = int(input("Enter value: "))
xx  = int( "%s%s" % (x, x) )
xxx = int( "%s%s%s" % (x, x, x) )

result = x + xx + xxx
print("Second try")
print("Result:", result)