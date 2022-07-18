#!/usr/bin/env python3

task = """
Task:
Write a Python program to convert all units of time into seconds.
"""

print(task)

def d_to_sec(n):
  return n * h_to_sec(24)

def h_to_sec(n):
  return n * m_to_sec(60)

def m_to_sec(n):
  return n * 60

print("5 days is", d_to_sec(5), "seconds")
print("5 hours is", h_to_sec(5), "seconds")
print("5 minutes is", m_to_sec(5), "seconds")
print("5d 5h 5m is", d_to_sec(5)+h_to_sec(5)+m_to_sec(5), "seconds")