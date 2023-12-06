from itertools import permutations

def permutaciones_validas(n, m, lista_numeros):
    """
    Genera permutaciones válidas de números del 1 al 'n' excluyendo el número 'm',
    y verifica que estas permutaciones sean diferentes de las listas de 'lista_numeros'.

    Parametros:
    - n (int): El rango de números para generar permutaciones (1, 2, ..., n).
    - m (int): El número que debe excluirse de las permutaciones.
    - lista_numeros (list): Lista de listas que representan números a comparar con las permutaciones.

    Returns:
    - validas (list): Lista de permutaciones válidas que no coinciden con las listas de 'lista_numeros'.
    """
    
    # Generar lista de números del 1 al 'n' excluyendo 'm'
    auxiliares = [i for i in range(1, n + 1) if i != m]
    validas = []  # Lista para almacenar permutaciones válidas
    permutaciones = []  # Lista para almacenar todas las permutaciones posibles
    
    # Generar todas las permutaciones posibles de la lista 'auxiliares'
    for permutacion in permutations(auxiliares):
        for i in range(n):
            # Rotar la permutación y convertirla en lista
            permutaciones.append(list(permutacion[i:] + permutacion[:i]))

    # Verificar la validez de cada permutación con respecto a 'lista_numeros'
    for permutacion in permutaciones:
        for numeros in lista_numeros:
            validez = True

            # Verificar cada número en la permutación
            for i in range(len(numeros)):
                if permutacion[i] == numeros[i]:
                    validez = False
                    break

            # Si se encuentra una coincidencia, salir del bucle interno
            if not validez:
                break

        # Si la permutación es válida y no está en la lista de permutaciones válidas, agregarla
        if validez and list(permutacion) not in validas:
            validas.append(list(permutacion))

    return validas

# Ejemplo de uso:
n = 4
m = 2
lista_numeros = [[1, 3, 2, 4], [4, 1, 3, 2]]
resultado = permutaciones_validas(n, m, lista_numeros)
print(resultado)
