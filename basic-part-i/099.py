#!/usr/bin/env python3

from os import system, name
from time import sleep

task = """
Task:
Write a Python program to clear the screen or terminal.
"""

print(task)

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


sleep(3)
clear_screen()