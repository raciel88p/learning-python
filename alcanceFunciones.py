# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 20:10:39 2021

@author: 50689
"""


#alcance de las funciones

def func1(un_arg, una_func):
    def func2(otro_arg):
        return otro_arg * 2
    
    valor = func2(un_arg)
    return una_func(valor)

un_arg = 1

def cualquier_func(cualquier_arg):
    return cualquier_arg + 5

print(func1(un_arg, cualquier_func))


""" Aca tenemos varios  funciones una dentro de otra unas son globales y otras son
locales el codigo se ejecuta de arriba hacia abajo de izquierda a derecha

fun1 
fun2
return otro_arg
cualquier_func 


con este comillas llamados doxtris especificamos el codigo a otros programadores
"""

help()