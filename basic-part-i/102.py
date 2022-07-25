#!/usr/bin/env python3

task = """
Task:
Write a Python program to get system command output.
"""

print(task)

def get_command_output(cmd):
    from os import popen
    return popen(cmd).read()

command = str("ls -lha {}".format(__file__))

print("""
Running command:
{}

Command output:
{}
""".format(command, get_command_output(command)))