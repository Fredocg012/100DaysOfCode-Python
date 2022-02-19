# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 06:26:03 2022

@author: pokem
"""
#Output

# Welcome to the tip calculator 
# What was the total bill? $124.54
# How many people to split the bill? 5
# What percentage tip would you like to give? 10, 12, or 15? 12
# Each person should pay $27.9


print("Welcome to the tip calculator!")

total = float(input("What was the total bill? $"))

people = int(input("How many people to split the bill? "))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

tip_calculation = tip / 100 * total + total

split_total = tip_calculation / people

rounded = round(split_total, 2)

message = f"Each person should pay: ${rounded}"

print(message)
