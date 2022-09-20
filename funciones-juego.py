# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD
Created on Tue Jun 21 20:32:51 2022
=======
Created on Tue Dec 14 19:38:27 2021
>>>>>>> c09d6c5c317b7a2963967f2221275a16198cf5f9

@author: 50689
"""


<<<<<<< HEAD
#funciones

def imprimir_mensaje():
    print('Mensaje especial')
    print('Estoy aprendiendo a usar funciones')
    
imprimir_mensaje()
imprimir_mensaje()

"""
print('Mensaje especial')
print('Estoy aprendiendo a usar funciones')
print('Mensaje especial')
print('Estoy aprendiendo a usar funciones')
print('Mensaje especial')
print('Estoy aprendiendo a usar funciones')
print('Mensaje especial')
print('Estoy aprendiendo a usar funciones')
"""
def conversacion (mensaje): #los parametros son las variable que vamos a usar dentro de la funci[on]
    print('Hola')
    print('Como estas')
    print(mensaje)
    print('Adios')
     
    
option = int(input('Elige una opcion: (1, 2, 3): '))
if option == 1:
    conversacion('Selecionaste la opcion 1')
elif option == 2:
    print('Hola')
    print('Como estas')
    print('Seleccionaste la opcion 2')
    print('Adios')
elif option == 3:
    conversacion('Selecionaste la opcion 3')
else:
    print('Elije la opcion correcta')
    
#funciones con un return
def suma(a, b):
    print('Se suman 2 numeros ')
    resultado = a + b
    return resultado

sumatoria = suma(25, 5)
print(sumatoria)
    
#convertidor  de monedas con funciones

def conversor(tipos_del_pesos, valor_del_dolar, valor_del_moneda_pais):
    # creamos primero las variables
    pesos = input('Cuantos pesos ' + tipos_del_pesos + ' tienes: ')
    pesos = float(pesos)
    #valor_dolar = 000.81
    dolares = pesos / valor_del_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $ ' + dolares + ' dolares ')
    #programa inverso convertir dolare a colones
    numero_1 = input(' Cuantos dolares tienes: ')
    dolares = float(dolares)
    #valor_del_colon = 700
    pesos = dolares * valor_del_moneda_pais
    pesos = round(pesos, 2)
    pesos = str(pesos)
    print('Tienes X monedas ' + pesos + ' '  + tipos_del_pesos)

menu = """ Bienvenido al conversor de monedas para varios paises

1- Moneda de Pesos Colombianos
2- Mondea de Costa Rica
3- Moneda de Pesos Mexico

"""

opcion = int(input(menu))

if opcion == 1: #Pesos Colombianos
    conversor('colombianos', 3865, 0.81)
elif opcion == 2: #Colones Costarricenses
    conversor('Costa Rica', 700, 715 )
elif opcion == 3: #Pesos Mexicanos
    # opcion primero las variables
    conversor('Mexico', 0.49, 287)
else:
    print("no tenemos mas opciones")
  
=======
# funciones y abstracciones

# las abstracciones no tenemos que conocer algo para poderlo utilizar

# Las funciones son mini programa que colaboran en conjunto para un programa mayor

def suma (a, b):
    total = a + b
    return total

print(suma(2,3))


def nombre_completo (nombre, apellido, inverso = False):
    if inverso: 
        return ( str(apellido), str(nombre))
    else:
        return (str(nombre), str(apellido))
    
nombre_completo("David", "Gullier")
nombre_completo("David", "Gullier", inverso = True)
nombre_completo(apellido="Gullier", nombre="David")

>>>>>>> c09d6c5c317b7a2963967f2221275a16198cf5f9
