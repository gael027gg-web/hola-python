def saludar(nombre):
    """
    Función simple que devuelve un saludo personalizado.
    
    Args:
        nombre (str): El nombre de la persona a saludar
        
    Returns:
        str: Un mensaje de saludo personalizado
    """
    return f"¡Hola, {nombre}!"


def sumar(a, b):
    """
    Función que suma dos números.
    
    Args:
        a (int/float): Primer número
        b (int/float): Segundo número
        
    Returns:
        int/float: La suma de a y b
    """
    return a + b


if __name__ == "__main__":
    print(saludar("Mundo"))
    print(f"2 + 3 = {sumar(2, 3)}")
