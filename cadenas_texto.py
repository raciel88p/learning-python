# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 17:36:26 2022

@author: 50689
"""

#poniendo la primer letra en mayuscula

nombre = input('Ingresa tu nombre: ')
nombre = nombre.upper()
print(nombre)
nombre = nombre.capitalize()
print(nombre)

#elminar espacio de un texto

nombre = nombre.strip()
print(nombre)

nombre = nombre.lower()
print(nombre)

nombre = nombre.replace('o', 'a')
print(nombre)

nombre[0]
print(nombre)

nombre[3]
print(nombre)

len(nombre)

#slides o rebanadas

nombre = 'Fransisco'

nombre[0:3]
print(nombre)

nombre[3:]
print(nombre)

nombre[1:7]
print(nombre)

nombre[1:7: 2] #pasos de 2 en 2
print(nombre)

nombre[::-1] #para ser en revesar una palabra
print(nombre)