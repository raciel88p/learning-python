# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 21:43:56 2021

@author: 50689
"""


#pruebas de caja de cristal

"""
Se basan en el flujo del programa

asumen que sabemos la implementacion

muy buenas para regresion testing o mocks

prueba los caminos posibles de uuna funcion
ramificacione, whily y recursione

"""

#importanto el modulo  de Unittest 
import unittest

#se asume que ya hay codigo escrito

def es_mayor_de_edad(edad):
    if edad > 18:
        return True
    else: 
        return False



class PruebaDeCristalTest(unittest.TestCase):
   # pass # null es llo que pasa
    #averiguando si la funcion se comporta de la manera correcta
    
    def test_es_mayor_de_edad(self):
        edad = 20
        
        resultado = es_mayor_de_edad(edad)
        
        self.assertEqual(resultado, True)
        
    def test_es_menor_de_edad(self):
        edad = 15
        
        resultado = es_mayor_de_edad(edad)
        
        self.assertAlmostEqual(resultado, False)
    
if __name__ == "__main__":
    unittest.main()