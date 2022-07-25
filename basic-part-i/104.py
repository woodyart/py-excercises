#!/usr/bin/env python3

import os

task = """
Task:
Write a Python program to get the effective group id, effective user id, real group id, 
a list of supplemental group ids associated with the current process.
Note: Availability: Unix.
"""

print(task)

pid  = os.getpid()
euid = os.geteuid()
egid = os.getegid()
uid  = os.getuid()
gid  = os.getgid()
sgid = str(os.getgroups())

print("""
Current Process Info
* PID               : {:>5}
* Effective GID     : {:>5}
* Effective UID     : {:>5}
* Real GID          : {:>5}
* Real UID          : {:>5}
* Supplemental GIDS : {}
""".format(pid, egid, euid, gid, uid, sgid))