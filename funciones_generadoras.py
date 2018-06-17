


print([numero for numero in [1,2,3,4,5,6,7,8,9,0] if  numero%2 == 0])
print([numero for numero in range(0,9) if  numero%2 == 0])

def pare(n):
    for numero in range(n+1):
        if numero % 2 == 0:
            yield numero
pare(10)

for numero in pare(10):
    print(numero)

print([numero for numero in pare(10) if  numero%2 == 0])

par = pare(3)
print(next(par))
print(next(par))
lista = [1,2,3,4,5,6,7,8,9,0]
lista_iterable = iter(lista) # convertir una coleccion a iterable
print(next(lista_iterable))
