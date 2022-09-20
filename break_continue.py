# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 20:47:01 2022

@author: 50689
"""


def run():
    for contador in range(1, 1000):
        if contador %2 != 0:
            continue
        print(contador)
    
    for i in range(10000):
        if i == 5999:
            break
        print(i)
        
    ingreso_texto = input("Ingresa un texto: ")
    for letra in ingreso_texto:
        if letra == 'o':
            break
        print(letra)

if __name__ == '__main__':
    run()