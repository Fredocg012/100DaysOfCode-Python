# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 00:50:31 2022

@author: pokem
"""

"""
Congratulations, you've got a job at Python Pizza.
Your first job is to build an automatic pizza order
program.

Based on a user´s order, work out their final bill.

- Small Pizza: $15. (S)
- Medium Pizza: $20. (M)
- Large Pizza: $25. (L)
- Pepperoni for small pizza: +$2 (Y or N)
- Pepperoni for Medium or Large Pizza: +$3 (Y or N)
- Extra cheese for any size pizza: +$1 (Y or no)

"""

pizza = input("Tamaño de pizza: ")

if pizza == 'S':
    costo = int(15)

elif pizza == 'M':
    costo = int(20)
    
elif pizza == 'L':
    costo = int(25)
    
else:
    print("Datos inválidos")
    
pepperoni = input("¿Con pepperoni? ")
    
if ((pepperoni == 'Y') and (pizza == 'S') ):
    costo = costo + 2
    
if ((pepperoni == 'Y') and ((pizza == 'M') or (pizza == 'L')) ):
    costo = costo + 3

elif pepperoni == 'N':
    costo = costo
else:
    print("Datos inválidos")

queso = input("¿Con queso extra? ")
    
if queso == 'Y':
    costo = costo + 1

if queso == 'N':
    costo = costo
    
else:
    print("Datos inválidos")
    
print(f"El costo final es: {costo}")
