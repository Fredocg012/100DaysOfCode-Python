# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 09:22:53 2022

@author: pokem
"""

"""
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.
"""

nombre_1 = input("Dame el primer nombre: ")
nombre_2 = input("Dame el segundo nombre: ")

nombre_1 = nombre_1.lower()
nombre_2 = nombre_2.lower()

T = nombre_1.count('t') + nombre_2.count('t')
R = nombre_1.count('r') + nombre_2.count('r')
U = nombre_1.count('u') + nombre_2.count('u')
E = nombre_1.count('e') + nombre_2.count('e')

valor_1 = T + R + U + E

L = nombre_1.count('l') + nombre_2.count('l')
O = nombre_1.count('o') + nombre_2.count('o')
V = nombre_1.count('v') + nombre_2.count('v')
E = nombre_1.count('e') + nombre_2.count('e')

valor_2 = L + O + V + E

puntuacion = str(valor_1) + str(valor_2)
puntuacionFinal = int(puntuacion)

if (puntuacionFinal < 10 and puntuacionFinal > 90):
    print(f"Su puntuación es: {puntuacionFinal}, ustedes juntos son como coca cola y mentas")
    
if (puntuacionFinal > 40 and puntuacionFinal < 50):
    print(f"Su puntuación es: {puntuacionFinal}, ustedes están muy unidos")
    
else:
    print(f"Su puntuación es: {puntuacionFinal}")
    

 
