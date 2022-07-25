#!/usr/bin/env python3

task = """
Task:
Write a Python program to list the special variables used within the language.
"""

print(task)

s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
print( '\n'.join(' '.join(s_var_names[i:i+8]) for i in range(0, len(s_var_names), 8)) )