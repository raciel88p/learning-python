# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 18:13:57 2021

@author: 50689
"""

"""
Funciones como objetos

"""

"""La primer funcion va a multipilcar el parametro por 2"""
def multiplicar_por_dos(n):
    return n * 2


"""La segunda funcion va a sumar 2 al parametro n"""
def sumar_dos(n):
    return n + 2


#la funcion mas importante
    
""
def aplicar_operacion(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)

        
    nums = [1, 2, 3]
    
    #llama la funcion de multiplicar + la funcion de operacion
    aplicar_operacion(multiplicar_por_dos, nums)
    [2, 4, 6]
    
    #llama a ala funcion de suma + la funcion de operacion
    aplicar_operacion(sumar_dos, nums)
    [3, 4, 5]
    

#Funciones en expresiones 

sumar = lambda x, y: x + y

sumar(2,3)

#funciones esn estructura de datos

def aplicar_operaciones(num):
    operaciones = [abs, float]
    
    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))
        
    return resultado

    aplicar_operaciones(-2)
    [2, -2.0]
    