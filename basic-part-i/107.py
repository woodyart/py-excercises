#!/usr/bin/env python3

from pathlib import Path
from time import ctime

task = """
Task:
Write a Python program to retrieve file properties.
"""

print(task)

f = Path(__file__)

mode  = oct(f.stat().st_mode)
uid   = f.stat().st_uid
gid   = f.stat().st_gid
size  = f.stat().st_size
mtime = ctime(f.stat().st_mtime)

print("""
| Mode     |  UID  |  GID  | SIZE  | MTIME                    | NAME
| {:8} | {:>5} | {:>5} | {:>5} | {:<24} | {}
""".format( mode, uid, gid, size, mtime, f.name))