# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 22:09:27 2021

@author: 50689
"""


#for son bucles definidos

frutas = ["manzana", "pera" , "uva", "banano"]
for frutas in frutas:
    print(frutas)
    
    
iter("cadenea") #cadena
iter(["a", "b", "c"])#lista
iter(("a", "b", "c"))#tupla
iter({"a", "b", "c"}) #conjunto
iter({"b": 1, "c": 3})#dicionario

frutas = ["manzana", "pera" , "uva", "banano"]
print(frutas)
iterador = iter(frutas)
next(iterador)
print(iterador) #manzana
next(iterador)
print(iterador) #pera
next(iterador)
print(iterador) #uva

estudiantes = {
    "Costa Rica": 100, 
    "Mexico": 50,
    "Puerto Rico": 10
    }
for pais in estudiantes:
    print(estudiantes)
    
for pais in estudiantes.keys():
    print(estudiantes)

for numero_de_estudiantes in estudiantes.values():
    print(estudiantes)
    break
for pais, numero_de_estudiantes in estudiantes.items():
    print(estudiantes)
    

    