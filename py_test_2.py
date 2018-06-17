def doblar(lista):
    """ Funcion doblar  
    >>> l = [1, 2, 3, 45, 56]
    >>> doblar(l)
    [2, 4, 6, 90, 112]
    
    >>> l = []
    >>> for i in range(10):
    ...     l.append(i)
    >>> doblar(l)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
 

    """
    return [n*2 for n in lista]


def suma(a,b):
    """ suma excepcion
    pueden ser numeros
    >>> suma(4,3)
    7

    >>> suma(5,5)
    10

    o cadenas de txto

    >>> suma('ave',' maria')
    'ave maria'

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> suma(a,b)
    [1, 2, 3, 4, 5, 6]
     controlando una execpcion 
    >>> suma(10,'hola')
    Traceback (most recent call last):
       ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
 
    """
    return a+b

if __name__ == "__main__":
    import doctest
    doctest.testmod()