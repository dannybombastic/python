
import random
import math

def leer_numero(ini,fin,msg):
    while True:
        try:
         valor = int( input( msg ) )        
        except:
            print("Error: Numero no valido")         
        else: 
              if valor <= fin and valor >= ini:
                  break
    return valor

def generador():
    numeros = leer_numero(1,20,"¿cuantos numero quieres generar [1-20]")
    modo = leer_numero(1,3,"¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")
    lista = []

    for i in range(numeros):
       numero =random.uniform(0,101)
       if modo == 1:
           print( "{} => {}".format( numero,math.ceil( numero ) ) )
           numero = math.ceil( numero )
       elif modo == 2:
           print( "{} => {}".format( numero,math.floor( numero ) ) )
           numero = math.floor( numero )
       elif modo == 3:
           print( "{} => {}".format( numero,round( numero ) ) )
           numero = round( numero )
          
generador()
