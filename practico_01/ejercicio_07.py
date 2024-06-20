"""Slicing."""


def es_palindromo(palabra: str) -> bool:
    """Toma un string y devuelve un booleano en base a si se lee igual al
    derecho y al revés.

    Restricción: No utilizar bucles - Usar Slices de listas.
    Referencia: https://docs.python.org/3/tutorial/introduction.html#lists
    """

    return palabra == palabra[::-1]

    pass # Completar


# NO MODIFICAR - INICIO
assert not es_palindromo("amor")
assert es_palindromo("radar")
assert es_palindromo("")
# NO MODIFICAR - FIN


###############################################################################


def mitad(palabra: str) -> str:
    """Toma un string y devuelve la mitad. Si la longitud es impar, redondear
    hacia arriba.

    Restricción: No utilizar bucles - Usar Slices de listas.
    Referencia: https://docs.python.org/3/tutorial/introduction.html#lists
    """

    length = len(palabra)
    half = length % 2
    if half == 0:
        half = length // 2
    else:
        half = length // 2 + 1
    return palabra[:half]

    ######VERSION OPTIMIZADA#######
    #   length = len(palabra)     #
    #   half = (length + 1) // 2  #
    #   return palabra[:half]     #
    ######VERSION OPTIMIZADA#######

    pass # Completar


# NO MODIFICAR - INICIO
assert mitad("hello") == "hel"
assert mitad("Moon") == "Mo"
assert mitad("") == ""
# NO MODIFICAR - FIN
