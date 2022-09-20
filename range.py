# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 21:33:37 2021

@author: 50689
"""


"""
Los Rangos

Secuencias de enteros

rango ( comienzo, fin, pasos)

son inmutables no se puede cambiar su valor

son buenos para contemplar la 
memoria y los for loops

"""
# range(comienzo, fin, pasos)

my_range = range(1, 5)
print(type(my_range))

for i in my_range:
    print(i)
    
my_range = range(0, 7, 2)
my_other_range = range (0, 8, 2)

print(my_range == my_other_range) #comparativo de valor
  

for p in my_range:
    print(p)
    
for i in my_other_range:
    print(i)
    
#como saber donde se guardo en memoria
    
print(id(my_range))
print(id(my_other_range))

#operador logico  para chekiar el valor de las memorias
print(my_range is my_other_range) #son memorias diferentes

# jungando con for y range
for i in range(0, 101, 4):
    print(i+1)
