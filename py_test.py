def palindromo(palabra):
    """ funcion palindromo
    
    >>> palindromo("radar")
    True

    >>> palindromo("somos")
    True

    >>> palindromo("loquesea")
    False

    >>> palindromo("Ana")
    True
    
    >>> palindromo("Atar a la rata")
    True
    """

    if palabra.lower().replace(" ","") == palabra[::-1].lower().replace(" ",""):
        return True
    else:
        return False


if __name__ == "__main__":
     import doctest
     doctest.testmod()