# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 15:40:47 2022

@author: 50689
"""

menu = """
    haga una ecucacion matamatica escoja un los siguientes simbolos
    1 para suma
    2 para restar
    3 para dividir 
    4 para multiplicar

"""
suma = 1
resta = 2
dividir  = 3
multiplicar = 4


def run():
    numero_1 = int(input('Ingrese un número matemático: '))
    opcion = int(input(menu))
    if opcion == 1: #suma
        suma = '+'
    elif opcion == 2: #resta
        resta = '-'
    elif opcion == 3: #division
        dividir  = '/'
    elif opcion == 3: #multiplicar
        multiplicar = '*'    
    else:
        print("por favor, ingrese un simbolo matemático")
    numero_2 = int(input('Ingrese un número matemático: '))

    calculadora(numero_1, opcion, numero_2)

def calculadora(numero_1, opcion, numero_2):
    if opcion == suma:
        print(numero_1 + numero_2)
    elif opcion == resta:
        print(numero_1 - numero_2)
    elif opcion == dividir:
        print(numero_1 / numero_2)
    elif opcion == multiplicar:
        print(numero_1 * numero_2)
    else:
        print('Por favor, escoje algún número')
    
if __name__ == '__main__':
    run()