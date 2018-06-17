from io import open
import pickle

class Personaje:

    def __init__(self,name,vida,ataque,alcance):
          self.name = name
          self.vida = vida
          self.ataque = ataque
          self.alcance = alcance

    def __str__(self):
       return "name : {} \nlife : {} \n atack : {} \nscope : {}".format(self.name,self.vida,self.ataque,self.alcance)


class Gestor:
    
    personaje = []
    
    # Constructor de clase
    def __init__(self):
        self.cargar()
        
    def agregar(self,p):
       for per in self.personaje:
            if per.name == p.name:
                    return 
            
            
       self.personaje.append(p)
       self.guardar()

    def borrar(self,name):
       for per in self.personaje:
           if per.name == name:
                  self.personaje.remove(per)
                  self.guardar()
                  return
            
            
       
        
    def mostrar(self):
        for p in self.personaje:
            print(p)
            
    def cargar(self):
        fichero = open('personas.txt','ab+')
        fichero.seek(0)
        try:
            self.personaje = pickle.load(fichero)
        except:
            print("El fichero esta vacio")
        finally:
            fichero.close()
            print("Se han cargado {} de peliculas".format(len( self.personaje )))
            
    def guardar(self):
        fichero = open('personas.txt','wb')
        pickle.dump(self.personaje,fichero)
        print("El fichero esta vacio")
        fichero.close()
        print("Se han cargado {} de personajes".format(len( self.personaje )))
    
    def __del__(self):
        self.guardar()
        



gest = Gestor()

gest.agregar(Personaje("caballero",4,2,4))
gest.agregar(Personaje("Arquero",5,2,4))
gest.agregar(Personaje("Mago",4,5,8))
gest.mostrar()
gest.borrar("Mago")
gest.mostrar()