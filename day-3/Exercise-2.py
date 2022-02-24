# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 23:50:19 2022

@author: pokem
"""
"""
 Write a program that interprets the Body Mass Index (BMI) 
 based on a user´s weight and height
"""

# Under 18.5 they are underweight.
# Over 18.5 but below 25 they have a normal weight.
# Over 25 but below 30 they are slightly overweight.
# Over 30 but below 35 they are obese.
# Above 35 they are clinically obese.

peso = float(input("Tu peso en kilogramos: "))
altura = float(input("Tu altura en metros: "))

bmi = peso /(altura * altura)

if(bmi < 18.5):
    print("Estás bajo de peso.")

elif(bmi >= 18.5 and bmi < 25 ):
    print("Estás normal de peso.")
    
elif(bmi >= 25 and bmi < 30):
    print("Estás ligeramente con sobrepeso")
    
elif(bmi >= 30 and bmi < 35):
    print("Tienes sobrepeso")

elif(bmi > 35):
    print("Tienes mucho sobrepeso")
    
    
    
