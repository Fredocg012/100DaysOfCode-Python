# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 00:43:03 2022

@author: pokem
"""

# Año bisiesto
#  Is evenly divisible by 4.
# Except every yearthat is divisible by 100
# unless the year is aslo divisible by 400

anio = int(input("Introduce el año: "))

if ((anio % 4 == 0) and (anio % 100 != 0)):
    print("Es año bisiesto")
    
elif ((anio % 400 == 0)):
    print("Es año bisiesto")
    
else:
    print("No es año bisiesto")