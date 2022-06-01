# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 19:35:43 2021

@author: 50689
"""


#Tuplas

"""
Caracteristica de la tuplas

secuencias inmutable de objetos

Puede contener cualquier tipo de objeto
y eso entran las funciones

Se pueden usar para devolver varios valores
en una funcion
"""

my_tuple = () #esto es una tupla vacia
print(type(my_tuple))


my_tuple = (1, "dos", False)
print(my_tuple[0])
#1
print(my_tuple[1])

"""importante no puede haber un error de codigo y para el programa

my_tuple[0] = 2
print(my_tuple[0])
# la tuplas son inmutable no se pueden cambiar su valor
"""
# tupla de un solo valor

my_tuple = (1) #esto no es una tupla es un error
print(type(my_tuple))
#int  

#para definir una tupla es necesario la ,
my_tuple = (1,)
print(type(my_tuple))

my_other_tuple = (2, 3, 4)
my_tuple += my_other_tuple #reasignamos la tupla
print(my_tuple)

#desampaquetando una tupla

x, y, z = my_other_tuple
print(x)
print(y)
print(z)

# regresando valores de una funcion
def coordenadas():
    return (5, 4)

coordenada = coordenadas()
print(coordenada)

x, y = coordenadas()
print(x, y)

