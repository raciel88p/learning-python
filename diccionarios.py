# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 15:21:55 2021

@author: 50689
"""


#Diccionarios

"""
ingresan a travez de llavez
no tienen un orden interno
pueden iterarse
se puueden cambiar

"""

#creo el diccionari
my_diccionario = {
        "David" : 35,
        "Erika" : 33,
        "Jaime" : 50,
    }

#Conociendo el valor de Jaime
print(my_diccionario["Jaime"])

#si no existe el valor pero tenems que acceder
my_diccionario.get("Juan", 30)

#reaccionado un valor
my_diccionario["Jaime"] = 20
print(my_diccionario)

#agregando un valor al diccionario
my_diccionario["Pedro"] = 25

#borrando valores del diccionario
del my_diccionario["Erika"]
print(my_diccionario)



#como iterar en el direccionario
#llama las llaves
for llave in my_diccionario.keys():
    print(llave)  

#llama los valores de las llaves
for valor in my_diccionario.values():
    print(valor)  

#llamar a la llave y el valor
for llave, valor in my_diccionario.items():
    print(llave, valor)
    
#saber si existe una llave en el diccionario
print("Roger" in my_diccionario)
