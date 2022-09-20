# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 19:02:55 2021

@author: 50689
"""


#Pruebas de caja negra o bugs

"""
Especificacion de la funcion

mandamos inputs y validamos outputs

Unit testing o integration testing

Garantia del codigo es con el unittest

"""
#importamos el modulo
import unittest

#declaramo la funcion suma
def suma(nume_1, nume_2):
    #pass // es un numero none
    return nume_1 + nume_2


#hacemos un clase
class CajaNegraTest(unittest.TestCase):
    """
    sumar 2 numeros
    """
    def test_suma_dos_positivios(self):
        nume_1 = 10
        nume_2 = 5
        
        resultado = suma(nume_1, nume_2)
        
        self.assertEqual(resultado, 15)
        
    def test_suma_dos_negativos(self):
        nume_1 = -10
        nume_2 = -75
        
        resultado = suma(nume_1, nume_2)
        
        self.assertEqual(resultado, -85)

#ejecutando el modulo de testing
if __name__ == "__main__":
    unittest.main()
    