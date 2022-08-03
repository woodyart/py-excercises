#!/usr/bin/env python3

from urllib.request import urlopen
import xml.etree.ElementTree as ET
import itertools

task = """
Task:
Write a Python program to get the top stories from Google news.
"""

print(task)

def get_top_news(url, num):
    file = urlopen(url)
    root = ET.fromstring(file.read())
    file.close()

    top10 = itertools.islice(root.iter('item'), num)

    print("TOP {} STORIES FROM GOOGLE NEWS".format(num))
    for id, item in enumerate(top10):
        print('#{}:'.format(id+1))
        title = item.find('title').text
        link  = item.find('link').text
        time  = item.find('pubDate').text
        print("{}\n{}\nlink: {}".format(time, title, link))


url = "https://news.google.com/rss"
get_top_news(url, 10)