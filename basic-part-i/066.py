#!/usr/bin/env python3

task = """
Task:
Write a Python program to calculate body mass index.
"""

print(task)

def bmi(mass, height):
    return round(mass/height**2, 1)

mass = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))


print("BMI (kg/m^2):", bmi(mass, height))