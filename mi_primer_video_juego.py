# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 19:39:04 2022

@author: 50689
"""

#juego de adivinanzas

import random 

def run():
   numero_aleatorio = random.randint(1, 100)
   numero_elegido = int(input('Ingrese y adivine un número entre el 1 y el 100: '))
   while numero_elegido != numero_aleatorio:
       if numero_elegido < numero_aleatorio:
           print('Busca un número más grande')
       elif numero_elegido > numero_aleatorio:
           print('Busca un número más pequeño')
       numero_elegido = int(input('Elije otro número: '))
   print('Ganaste')
        
if __name__ == '__main__':
    run()