#!/usr/bin/env python3

from urllib import request

task = """
Task:
Write a Python program to access and print a URL's content to the console.
"""

print(task)

def get_data_urlib(url):
    weburl = request.urlopen(url)
    return weburl.read()

url = "https://docs.python.org/3/library/urllib.html"

print(get_data_urlib(url))