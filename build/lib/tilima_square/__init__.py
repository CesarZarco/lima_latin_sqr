def my_sum(x, y):
    """A function that sums. """
    return x+y


def my_mul(x, y):
    """A function that multiply. """
    return x*y

import itertools

def generar_todos_los_cuadrados_latinos(n):
    # Genera una lista de números del 1 al n
    numeros = list(range(1, n + 1))

    # Genera todas las permutaciones posibles de esa lista
    cuadrados_latinos = []
    for permutacion in itertools.permutations(numeros):

        # Crea un cuadrado latino al añadir la permutación a sí misma, pero en orden inverso
        cuadrado_latino = [permutacion[i:] + permutacion[:i] for i in range(n)]

        # Verifica si el cuadrado latino ya ha sido generado
        # Si el cuadrado latino ya ha sido generado, lo omitirá
        if cuadrado_latino not in cuadrados_latinos:
            cuadrados_latinos.append(cuadrado_latino)

    # Devuelve la lista de cuadrados latinos generados
    return cuadrados_latinos
