import math

def suma(a,b):
    try:
       r = a + b
    except TypeError:
       print("Error tipo de dato no soportado")
    else:
       return r

def resta(a,b):
    try:
       r = a - b
    except TypeError:
       print("Error tipo de dato no soportado")
    else:
       return r

def division(a,b):
    try:
       r = a / b
    except TypeError:
       print("Error tipo de dato no soportado")
    except ZeroDivisionError:
         print("No se puede dividir por 0")
    else:
       return r

def producto(a,b):
    try:

       r = a * b

    except TypeError:
       print("Error tipo de dato no soportado")
    else:
       return r

number = input("")