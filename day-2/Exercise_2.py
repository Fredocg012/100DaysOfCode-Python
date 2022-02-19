# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 05:51:14 2022

@author: pokem
"""

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


peso = float(weight)
altura = float(height)



bmi = peso/(altura * altura)
print(round(bmi))
