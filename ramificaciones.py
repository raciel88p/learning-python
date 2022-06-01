# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 16:48:46 2021

@author: 50689
"""

#ramificaciones o desiciones

num_1 = int(input("Ingresa un numero: "))
num_2 = int(input("ingresa otro numero: "))
#num_3 = int(input("Ingresa un operador matematico: "))

if num_1 >  num_2:
    print("numero 1 es mayor que numero 2")
elif num_2 == num_1:
    print("numero 2 es igual a numero 1")
else:
    print("son numeros diferentes")


#reto de platzi
    
pregunta_nombre1 = input("ingresa tu nombre: ")
pregunta_edad1 = int(input("ingresa tu edad: "))
pregunta_nombre2  = input("ingresa tu nombre: ")
pregunta_edad2 = int(input("ingresa tu edad: "))

if pregunta_edad1  > pregunta_edad2:
    print (pregunta_nombre1 + " es mayor " + pregunta_nombre2)
elif pregunta_edad1 < pregunta_edad2:
    print (pregunta_nombre2 + " es mayor " + pregunta_nombre1)
else:
    print(pregunta_nombre1 + " tienen la misma edad que " + pregunta_nombre2)