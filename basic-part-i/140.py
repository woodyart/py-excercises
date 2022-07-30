#!/usr/bin/env python3

import ipaddress

task = """
Task:
Write a Python program to convert an integer to binary keep leading zeros.
"""

print(task)

x = int(input("Enter value: "))
print( 'First try  :', x, '=', str(bin(x)[2:]).rjust(10, '0') )
print( 'Second try : {} = {:010b}'.format(x, x) )