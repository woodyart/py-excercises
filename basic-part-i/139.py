#!/usr/bin/env python3

import ipaddress

task = """
Task:
Write a Python program to valid a IP address.
"""

print(task)

try:
    ip = ipaddress.ip_address(input("Enter IP: "))
    print("IP address valid")
except:
    print("IP address is not valid")