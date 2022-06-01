# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 21:33:12 2021

@author: 50689
"""

"""  Recursividade algoritmica y programatica

algoritmica es encontrar soluciones con la funcion de divide  y venceras es un problema grande 
lo podemos hacer pequeno, un problema base 

programatica que es una funcion que se llama asi misma.

Los factoriales:
    
    escribir comentarios antes de programacion

 """
 
def factorial(n):
     """ 
     Calcula el factorial de n
     
     n int >  0
     return n! 
     
     """
     print(n)
     if n == 1:
         return 1
     
     return n * factorial(n - 1)


n = int(input("Escribe un numero: "))

print(factorial(n))


"""
 Algoritmo de fibonachi  en la recursividad
"""
def fibonacci(n):
    print(n)
    if n == 0 or n ==1:
        return 1
    #print(n)
    return fibonacci( n - 1) + fibonacci(n - 2)
n = int(input("Escribe un numero entero: "))

print("El numero fibonacci para " + str(n) + " es " + str(fibonacci(n)))