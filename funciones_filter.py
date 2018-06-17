numeros = [1,2,3,4,5,6,7,8,9,0]
def multiple(numero):
    if numero % 5 == 0:
        return True

filtro = filter(multiple,numeros)
#lista = list(filtro)
print(next(filtro))
print(list(filter( lambda numero : numero % 2 == 0, numeros )))
#print(lista)




class Person:

    def __init__(self,nombre,edad):

        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return "name: {}\t age: {}".format(self.nombre,self.edad)



personas =[
    Person("manu",34),
    Person("antonio",54),
    Person("jose",26),
    Person("david",13)
]

compare = lambda p_1: p_1.edad > 18
iterador = filter(compare,personas)
print(next(iterador))
print(next(iterador))
print(next(iterador))

