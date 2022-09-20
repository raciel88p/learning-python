# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 19:33:51 2021

@author: 50689
"""


#aproximacion de soluciones
# canje entre presion a rápidos


objetivo = int(input("Escoje un numero: "))
epsilon = 0.0001 # tarda mas de una hora
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    #para conocer que pasa dentro del algoritmo
    print(abs(respuesta**2 - objetivo), respuesta) #como se mueve la respuesta al final
    respuesta += paso
if abs(respuesta**2 - objetivo) >= epsilon:
    print("No se escontro la raiz cuadrada del objetivo " + str(objetivo))
else:
    print("Encontramos la raiz cuadrada del " + str(objetivo) + "es la " +str(respuesta))