numeros = [1,2,3,4,5,6,7,8,9,0]
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


personas2 =[
    Person("alejandro",34),
    Person("falete",54),
    Person("pepe",26),
    Person("goliat",13)
]

# sin instanciar t da igual que calcule la suma del la longitud  o que obtenga los valores 
# directamente accediendo con el "." a los atributos edad o nombre me funciona iguial :) 
dobla_edad = lambda a,b: len(a.nombre)+len(b.nombre)
suma_edad = lambda persona: Person(persona.nombre,persona.edad+1)  
people = map( lambda a,b: len(a.nombre)+len(b.nombre), personas, personas2)
people = map(suma_edad,personas)
pope = list(people)
for p in pope:
    print(p.nombre)

def doblar(num):
    if num == 0:
        num = num+2
        return num
    return num*2

m = map(doblar,numeros)
print(list(m))
n = map(lambda x: x*2,numeros)
print(list(n))
a = [1,2,3,4,5,6,7,8,9,0]
b = [1,2,3,4,5,6,7,8,9,0]
producto = map(lambda a,b: a*b, a, b)
print(list(producto))