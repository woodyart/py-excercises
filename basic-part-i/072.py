#!/usr/bin/env python3

import importlib


task = """
Task:
Write a Python program to get the details of math module.
"""

print(task)

def get_module_info(module_name):
    m_name = importlib.import_module(name=module_name)
    return help(m_name)

def get_module_info_hard(module_name):
    m_name = importlib.import_module(name=module_name)
    for item in dir(m_name):
        print('\n===========\n' ,item, '\n===========\n' ,item.__doc__)

print(get_module_info("math"))
print(get_module_info_hard("math"))