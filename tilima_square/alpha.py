import itertools
from sympy import Matrix, init_printing
init_printing(use_latex=True)

def generar_todos_los_cuadrados_latinos_letras(n):
    # Genera una lista de números del 1 al n
    # numeros = list(range(1, n + 1))
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    letras = list(alfabeto[:n])
    # Genera todas las permutaciones posibles de esa lista
    cuadrados_latinos = []
    for permutacion in itertools.permutations(letras):

        # Crea un cuadrado latino al añadir la permutación a sí misma, pero en orden inverso
        cuadrado_latino = Matrix([list(permutacion[i:] + permutacion[:i]) for i in range(n)])

        # Verifica si el cuadrado latino ya ha sido generado
        # Si el cuadrado latino ya ha sido generado, lo omitirá
        if cuadrado_latino not in cuadrados_latinos:
            cuadrados_latinos.append(cuadrado_latino)

    # Devuelve la lista de cuadrados latinos generados
    return cuadrados_latinos

# Ejemplo
cuadrados_latinos = generar_todos_los_cuadrados_latinos(3)
cuadrados_latinos
# Imprime los cuadrados latinos generados
#print(cuadrados_latinos)

#len(cuadrados_latinos)
