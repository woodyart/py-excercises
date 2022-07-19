#!/usr/bin/env python3

task = """
Task:
Write a Python program to convert pressure in kilopascals to:
- pounds per square inch
- a millimeter of mercury (mmHg)
- atmosphere pressure
"""

print(task)

def kpa_to_psi(kpa):
    return round(kpa * 0.145038, 3)

def kpa_to_mmhg(kpa):
    return round(kpa * 7.50062, 3)

def kpa_to_atm(kpa):
    return round(kpa * 0.00987, 3)

kpa = float(input("Enter pressure (kPa): "))

print("""
{} kPa:
    - {} PSI
    - {} mmHg
    - {} Atm
""".format(kpa, kpa_to_psi(kpa), kpa_to_mmhg(kpa), kpa_to_atm(kpa)))