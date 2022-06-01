# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 12:47:25 2021

@author: 50689
"""


#listas y mutabilidad

"""
Lista que si podemos cambiar sus valores

Pueden tener efectos secundario cuando modificas una lista

Es posible iterar con ellas

lista.extend(iterable) #extiende la lista con valores dentro de un iterable como un range()
lista.insert(i, ‘valor’) #Agrega un valor en la posición i y recorre todos los demás. No borra nada.
lista.pop(i) #Elimina valor en la posición i de la lista.
lista.remove(‘valor’) #Elimina el primer elemento con ese valor.
lista.clear() #Borra elementos en la lista.
lista.index(‘valor’) #Retorna posición del primer elemento con el valor.
lista.index(‘valor’, start, end) #Retorna posición del elemento con el valor dentro de los elementos desde posición start hasta posición end)
lista.count(‘valor’) #Cuenta cuántas veces esta ese valor en la lista.
lista.sort() #Ordena los elementos de mayor a menor.
lista.sort(reverse = True) #Ordena los elementos de menor a mayor.
lista.reverse() #Invierte los elementos
lista.copy() #Genera una copia de la lista. También útil para clonar listas.

Pueden tener cualquire tipo de valor
"""

my_lista = [1, 2, 3]

print(my_lista[0]) #ingresando al indice de la lista

print(my_lista[1:]) #ingresando a los valores de lista desde 1 hacia adelante

#cambiando el valor de una lista
#alladienndo el valor de 4
my_lista.append(4)
print(my_lista)

my_lista[0] = "Esto cambio"
print(my_lista)

my_lista.pop() #elimino el 4 o el ultimo elemento
print(my_lista)

#podemos iterar una listta

for element in my_lista:
    print(my_lista)
    
# efectos secudarios de listas
lista_a = [1, 5, 7, 9] 
lista_b = lista_a #asinamos lista a a b

print(lista_a)
print(lista_b)

#esto es donde puede generar errores
print(id(lista_a))
print(id(lista_b))

lista_c = [lista_a, lista_b]
print(lista_c)

lista_a.append(5)

print(lista_c)
#errores mas comunes de errores








#como generar copias y clonar una lista
a = [1, 2, 3]
print(id(a))

b = a
print(id(b))

c = list(a) #clonar la lista a

print(a)
print(b)
print(c)


# van a tener los mismo valores

#pero diferente memmoria

print(id(a))
print(id(c))

#otra forma de hacer clonacion
#[ inicion: fin: secuencia]

d = a[::]
print(d)
print(id(d))







#List comprehension es forma consisa de aplicar operaciones a los valores de una lista
# y se puden aplicar condiciones


my_lista = list(range(100))
print(my_lista)

double = [ i * 2 for  i in my_lista]
print(double)

pares = [i for i in my_lista if i % 2 == 0]
print(pares)
