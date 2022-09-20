# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 21:39:02 2022

@author: 50689
"""

#while bucle

def run():
    LIMITE = 1000 #una variable constante que no cambia
    
    contador = 0
    potencia_2 = 2**contador
    potencia = (4+3 * 5)
    
    while potencia_2 < LIMITE:
        print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador
        
    while potencia <= 25:
        print('potencia es un numero ' + str(contador))
        contador = contador + 2
        break 
    
        
# entry point de la logica
if __name__ == '__main__':
    run()