#!/usr/bin/env python3

from ssl import get_protocol_name


task = """
Task:
Write a Python program to check the priority of the four operators (+, -, *, /).
"""

print(task)

__operators__ = { '+':0, '-':0, '*':1, '/':1 }

def get_priority(op1, op2):
    return __operators__[op1] > __operators__[op2]


print("+ has higher priority than * : ", get_priority('+', '*'))
print("+ has higher priority than - : ", get_priority('+', '-'))
print("* has higher priority than - : ", get_priority('*', '-'))
print("/ has higher priority than + : ", get_priority('/', '+'))
print("/ has higher priority than * : ", get_priority('/', '*'))