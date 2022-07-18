#!/usr/bin/env python3

from datetime import datetime as dt

task = """
Task:
Write a Python program to get file creation and modification date/times.
"""

print(task)

def get_file_meta_os(f):
    import os
    return os.stat(f).st_birthtime, os.path.getmtime(f)

def get_file_meta_pathlib(f):
    from pathlib import Path
    return Path(f).stat().st_birthtime, Path(f).stat().st_mtime

f = __file__
ctime, mtime = get_file_meta_os(f)
print("OS: {} created at {}, modified at {}".format(f, dt.fromtimestamp(ctime), dt.fromtimestamp(mtime)))

ctime, mtime = get_file_meta_pathlib(f)
print("Pathlib: {} created at {}, modified at {}".format(f, dt.fromtimestamp(ctime), dt.fromtimestamp(mtime)))