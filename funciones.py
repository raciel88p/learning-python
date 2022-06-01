# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 19:38:27 2021

@author: 50689
"""


# funciones y abstracciones

# las abstracciones no tenemos que conocer algo para poderlo utilizar

# Las funciones son mini programa que colaboran en conjunto para un programa mayor

def suma (a, b):
    total = a + b
    return total

print(suma(2,3))


def nombre_completo (nombre, apellido, inverso = False):
    if inverso: 
        return ( str(apellido), str(nombre))
    else:
        return (str(nombre), str(apellido))
    
nombre_completo("David", "Gullier")
nombre_completo("David", "Gullier", inverso = True)
nombre_completo(apellido="Gullier", nombre="David")

