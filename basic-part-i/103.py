#!/usr/bin/env python3

task = """
Task:
Write a Python program to extract the filename from a given path.
"""

print(task)

def get_filename_path(my_path):
    from pathlib import Path
    return Path(my_path).name

def get_filename_os(my_path):
    from os import path
    return path.basename(my_path)

print("""
Path                   : {}
File name with pathlib : {}
File name with os      : {}
""".format(__file__, get_filename_path(__file__), get_filename_os(__file__)))