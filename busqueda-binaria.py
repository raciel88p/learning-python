# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 20:14:22 2021

@author: 50689
"""


#Busqueda Binaria

objetivo = int(input("Escoje  un numero: "))
epsilon = 0.01
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = (alto + bajo) / 2

while abs(respuesta**2 - objetivo) >= epsilon:
    print(str(bajo), str(alto), str(respuesta)) # para ver las operaciones internamente
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    
    
    respuesta = (alto + bajo)/2
    
print("La raiz cuadrada del " + str(objetivo) + " es " + str(respuesta))