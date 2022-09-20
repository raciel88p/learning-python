# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 08:41:09 2022

@author: 50689
"""


#prueba de primalidad

#numero primo que se puede divir por si mismo y por 1

def es_primo(numero):
    contador = 0
    
    for i in range(1, numero+1):
        if 1 == 1 or 1 == numero:
            continue
        if numero % i == 0:
            contador += 1
     
    if contador == 0:
        return True
    else:
        return False
    
    
def run():
    numero = int(input("Escribe un número: "))
    if es_primo(numero):
        print(es_primo)
    else:
        print('no es primo')
        
if __name__ == '__main__':
    run()