# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 06:05:20 2022

@author: pokem
"""

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

dias = 365
semanas = 52
meses = 12

vidaDias = 90 * dias
vidaSemanas = 90 * semanas
vidaMeses = 90 * meses

diasPersona = int(age) * int(dias)
semanasPersona = int(age) * int(semanas)
mesesPersona = int(age) * int(meses)

diasRestantes = vidaDias - diasPersona
semanasRestantes = vidaSemanas - semanasPersona
mesesRestantes = vidaMeses - mesesPersona

print(f"You have {diasRestantes} days, {semanasRestantes} weeks, and {mesesRestantes} months left.")