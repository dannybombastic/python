lista = []
for letra in "casa":
    lista.append(letra)

lista =[letra for letra in "casa"]

# crear una lista de numeros con un rango de 12
lista = []
for numero in range(0,12):
    lista.append(numero**2)
print(lista)

# comprension de listas 
lista =[]
lista = [numero**2 for numero in range(0,13)]
print("lista de rango de 13",lista)
# comprension de listas 
lista =[]
lista = [numero for numero in range(0,12) if numero % 2 == 0]
print(lista)
# comprension anidada 

pares = [numero for numero in [numero**2 for numero in range(0,12) if numero > 4] if numero % 2 == 0]
print("pares :",pares)


def funcuionAnidada():

    def otra():
        return "hola desde la encapsulacion"
    return otra

# tipo funcion 
var = funcuionAnidada()
print(var())


def reciveFuncion(funcion):
    print(funcion())

reciveFuncion(var)

# decorators


def monitor(funcion):

    def decorar():
        print("antes",funcion.__name__)
        funcion()
        print("despues",funcion.__name__)
    return decorar 

@monitor
def saluda():
    print("recibe un saludo")
@monitor
def despide():
    print("adeu andreu")

# normal proccedure
# monitor(saluda)()

saluda()

def monitor_argvs(funcion):
    
    def decorar(*args,**kwargs):
        print("antes",funcion.__name__)
        funcion(*args,**kwargs)
        print("despues de {}".format(*args,**kwargs),funcion.__name__)
    return decorar 


@monitor_argvs
def saludar(texto):
    print("hola {}".format(texto))
@monitor_argvs
def despedir(texto):
    print("adeu {}".format(texto))

saludar("pepe")