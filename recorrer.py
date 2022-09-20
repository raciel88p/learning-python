# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 21:04:35 2022

@author: 50689
"""


# jungando con en cadenas de texto

def run():
    nombre = input('Ingrese su nombre: ')
    for letra in nombre:
        print(letra)
        
    frase = input('Escribe una frase: ')
    for caracter in frase:
      print(caracter.upper())  

if __name__ == '__main__':
    run()