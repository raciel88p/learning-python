# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 19:55:38 2021

@author: 50689
"""


#Enumeracion exhaustiva / adivina o verifca

objetivo = int(input("Escoje un entero: "))
respuesta = 0

while respuesta**2 < objetivo:
    respuesta += 1
    
if respuesta**2 == objetivo:
    print('la raiz cuadrada de ' + str(objetivo) + str(respuesta))
else:
    print(str(objetivo) + ' no tiene raiz cuadrada exacta')