# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 21:17:57 2021

@author: 50689
"""


cadena = "Esto es una cadena"
"123" * 3
"123" + "456"
("hip"  * 3) + " " + "hurra"
#f '{"hip " * 3} hurra'
print(cadena)

print(len(cadena))

print("18 representa la cantidad de caracteres de la variable")
print(cadena[0])

#comienzo final y pasos 

my_str = "Platzi"
prueba = len(my_str) # 6 caracteres
print(prueba)

prueba = my_str[0] #notacion de indice para aceder P
print(prueba)

prueba = my_str[1] # L
print(prueba)

prueba = my_str[2:] # a
print(prueba)

prueba = my_str[:3] # slacing  o notacion de rebanada
print(prueba) #comienzo final y cuantos pasos vamos a saltar

prueba = my_str[:-2] # iniamos atras
print(prueba)

prueba = my_str[::2] # saltando de 2 en2
print(prueba)

texto = 'yo amo programar en' + " " + my_str
print(texto)

cosa = f"Yo amo a {my_str},"  * 100
print(cosa)


