# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 12:28:25 2021

@author: 50689
"""


#manejando excepciones o errores de progra

def divide_elementos_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e) #para ver que hay dentro del error
        return lista

        
lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))