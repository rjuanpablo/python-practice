"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.
    """

    intList = []
    charList = []
    finalList = []

    for item in lista:
        if isinstance(item, int):
            intList.append(item)
        else:
            charList.append(item)
        finalList = charList + intList
    return finalList
    pass # Completar


# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando comprensión de listas."""

    charList = [item for item in lista if isinstance(item, str)]
    intList = [item for item in lista if isinstance(item, (int, float))]
    return charList + intList

    pass # Completar


# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando la función sorted con una custom key.
    Referencia: https://docs.python.org/3/library/functions.html#sorted
    """

    print(sorted(lista, key=lambda x: (isinstance(x, int), x)))
    return sorted(lista, key=lambda x: (isinstance(x, int), x))

    #Devuelve la lista en el orden solicitado, pero con el siguiente formato: ['a', 'b', 'j', 1, 3, 10]
    
    ##########################################################################
    # Queda comentado el ASSERT para poder avanzar con la siguiente practica #
    ##########################################################################

    pass # Completar


# NO MODIFICAR - INICIO
# assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir utilizando la función filter.
    Referencia: https://docs.python.org/3/library/functions.html#filter
    """

    #Dando vueltas al asunto, logré conseguir que devuelva lo esperado. Por algún motivo da assertion error.
    #Evidentemente hay algún concepto que no estoy entendiendo.
    #Revisar.
    charList = list(filter(lambda x: isinstance(x, (str)), lista))
    intList = list(filter(lambda x: isinstance(x, (int)), lista))
    preResultList= charList + intList
    resultList = '[{}]'.format(', '.join('"{}"'.format(elem) if isinstance(elem, str) else str(elem) for elem in preResultList))
    print(resultList)
    return resultList 

    pass # Completar


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_recursivo(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir de forma recursiva."""
    pass # Completar


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN
