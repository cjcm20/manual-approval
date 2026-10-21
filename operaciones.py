
def sumar(a: float, b: float) -> float:
    """
    Operacion de suma
    """
    return a + b


def dividir(a: float, b: float) -> float:
    """
    Operacion de dividir
    """
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def agrupar(elementos: list, tamano: int) -> list[list]:
    n = len(elementos)
    if n < tamano:
        return elementos
    count = -1
    agrupacion = {}
    for number, i in enumerate(elementos):
        if number % tamano == 0:
            count += 1
            agrupacion[count] = []
        agrupacion[count].append(i)

    return list(agrupacion.values())
