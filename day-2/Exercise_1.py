# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 05:41:29 2022

@author: pokem
"""

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

primerDigito = two_digit_number[0]
segundoDigito = two_digit_number[1]

resultado = int(primerDigito) + int(segundoDigito)

#print(f"{primerDigito} + {segundoDigito} = {resultado}" )
print(resultado)