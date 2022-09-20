# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 20:14:35 2022

@author: 50689
"""
menu = """ Bienvenido al conversor de monedas para varios paises

1- Moneda de Pesos Colombianos
2- Mondea de Costa Rica
3- Moneda de Pesos Mexico

"""

opcion = int(input(menu))

if opcion == 1: #Pesos Colombianos
    # creamos primero las variables
    pesos = input('Cuantos pesos argentinos tienes: ')
    pesos = float(pesos)
    valor_dolar = 000.81
    dolares = pesos / valor_dolar 
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $ ' + dolares + ' dolares ')
    #programa inverso convertir dolare a colones
    numero_1 = input(' Cuantos dolares tienes: ')
    dolares = float(dolares)
    valor_del_colon = 700
    pesos = dolares * valor_del_colon
    pesos = round(pesos, 2)
    pesos = str(pesos)
    print('Tienes X colones ' + pesos + ' pesos Argentinos ')
    
elif opcion == 2: #Colones Costarricenses
    # creamos primero las variables
    colones = input(' Cuantos colones tienes: ')
    colones = float(colones)
    valor_dolar = 700
    dolares = colones / valor_dolar 
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $ ' + dolares + ' dolares')
    #programa inverso convertir dolare a colones
    numero_1 = input('Cuantos dolares tienes: ')
    dolares = float(dolares)
    valor_del_colon = 700
    colones = dolares * valor_del_colon
    colones = round(colones, 2)
    colones = str(colones)
    print('Tienes X colones ' + colones + ' colones ')
elif opcion == 3: #Pesos Mexicanos
    # opcion primero las variables
    pesos = input('Cuantos pesos mexicanos tienes: ')
    pesos = float(pesos)
    valor_dolar = 0.49
    dolares = pesos / valor_dolar 
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $ ' + dolares + ' dolares ')
    #programa inverso convertir dolare a pesos mexicanos
    numero_1 = input('Cuantos dolares tienes: ')
    dolares = float(dolares)
    valor_del_colon = 20.23
    pesos = dolares * valor_del_colon
    pesos = round(pesos, 2)
    pesos = str(pesos)
    print('Tienes X pesos ' + pesos + ' pesos mexicanos ')
else:
    print("no tenemos mas opciones")

