# -*- coding: utf-8 -*-
"""
Created on Thu May  3 19:42:43 2018

@author: Vspc-PoisonRiver
"""

import sys

if len(sys.argv) == 2:
    numero = int( sys.argv[1])
    
    if numero < 0 or numero > 9999:
        print("Error - Numero es incorrecto")
        print("Ejemplo ",sys.argv[20:-7], "[0-9999]")
    else:
        cadena = str(numero)
        longitud = len(cadena)
        
        for i in range(longitud):
            print( "{:04d}".format( int( cadena[longitud-1-i]) * 10 ** i )  )
            
else:
    print("Error - Argumentos incorrectos")
    print("Ejemplo ",sys.argv[20:-7], "[0-9999]")