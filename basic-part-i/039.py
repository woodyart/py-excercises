#!/usr/bin/env python3

task = """
Task:
Write a Python program to compute the future value of a specified principal amount,
rate of interest, and a number of years.
"""

print(task)

def future_value(amt, int, years):
    # FV = PV * (1 + i)^n
    #   FV : Future Value
    #   PV : Present Value (amt)
    #    i : interest rate per period in decimal form (1/100 * int)
    #    n : number of periods (years)
    PV = amt
    i  = 1/100 * int
    n  = years
    FV = PV * (1 + i)**n
    return FV

amt = 10000
int = 3.5
years = 7

print(round(future_value(amt, int, years),2))