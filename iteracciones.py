# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 21:14:50 2021

@author: 50689
"""


#iteracciones o los loops indefinidos

contador = 0

while contador <= 10:
    print(contador)
    contador +=1 # esto es igual contador = contador + 1

contador_externo = 0
contador_interno = 1

while contador_externo < 5:
    while contador_interno < 32:
        print(contador_externo, contador_interno)
        contador_interno += 2
        
        #salirse de la operacion
        if contador_interno >= 3:
            break
        
    contador_externo += 1 
#hacer reset el contador interno
    contador_interno = 0
    
    #que pasa si se elimina el contador interno
    