#!/usr/bin/env python3

import socket

task = """
Task:
Write a Python to find local IP addresses using Python's stdlib.
"""

print(task)

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254', 9999))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

print("""
Note: the script just returns IP address of main interface in system,
because you can't just get all interfaces from any OS (Windows, MacOS, Linux) and extract their IPs in easy way.
Too hard for beginner.
""")
print(get_ip())