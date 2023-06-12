# Compresor Universal
def compress(elements, initial_value, operation):
    """
    Recibe una secuencia de elementos, un valor inicial y 
    una función que representa una operación de combinación
    de dos elementos.
    Devuelve un solo valor comprimido
    """
    accum = initial_value
    for element in elements:
        accum = operation(accum, element)
    return accum         

# Selector Universal
def select(elements: list, predicate)-> list:
    """
    Recibe una lista y un predicado. Devuelve una nueva lista con aquellos elementos
    que superan el test del predicado.
    """
    selected = []
    for element in elements:
        if predicate(element):
            selected.append(element)
    return selected

# Transformador Universal
def transform(elements:list, change_element) ->list :
    new_list = []
    for element in elements:
        new_list.append(change_element(element))
    return new_list
