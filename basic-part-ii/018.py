#!/usr/bin/env python3

task = """
Task:
Write a Python program to find the median among three given numbers.
"""

print(task)

def get_median(nums):
    nums = sorted(nums)
    length = len(nums)
    middle_id = (length - 1) // 2
    if length%2 == 0:
        median = (nums[middle_id] + nums[middle_id+1]) / 2.0
    else:
        median = nums[middle_id]
    return median


dataset = [ [1,3,5], [10,30,20], [90,5,12], [7,6,8] ]

for data in dataset:
    print("Median for {} is {}".format(data, get_median(data)))