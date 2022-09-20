# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 20:38:48 2022

@author: 50689
"""


#palíndromo

def palindromo(palabra):
    palabra = palabra.replace(' ', '') #eliminamos los espacios
    palabra = palabra.lower() #todo en minuscula
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False
    
# buena practia de python dejar 2 espacion entre cada funcion
def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es Palindromo')
    else:
        print('No es palindromo')
    
#punto de entrada al codigo   y es una buena practica
    
if __name__ == '__main__':
        run()
