from itertools import permutations, combinations
from sympy import Matrix

def square_permutations(n):
    """
    Generate a list of matrices of order N, all of which are Latin squares, using permutations from itertools.
    It does not show all possible latin squares of that order.

    Parameters:
    - N (int): The order of the matrix and the elements it will contain (1, 2, ..., n).

    Returns:
    - square_permutations(N): List of Latin squares that come from permutations as rows.
    
    Example
    ```python
    cuadrados_latinos = all_square_permutations(3)
    print(cuadrados_latinos)
    [[[1, 2, 3], [2, 3, 1], [3, 1, 2]],
    [[1, 2, 3], [3, 1, 2], [2, 3, 1]],...
    ```   
    """   
    # Generate a list of numbers form 1 to N
    numbers = list(range(1, n + 1))

    # With itertools generate all the permutations of the list
    latin_sqrs = []
    for permutation in permutations(numbers):

        # Make a latin square using a permutation, reorder the same permutaion moving the elements one
        # position then insert the new permutation as a row
        latin_sqr = [list(permutation[i:] + permutation[:i]) for i in range(n)]

        #Verifies whether the Latin square has been generated before.
        #If it has not been generated before, it will be added to the list latin_sqrs
        if latin_sqr not in latin_sqrs:
            latin_sqrs.append(latin_sqr)

        # Does the same than in the lines befor but in the inverse order
        latin_sqr = [list(permutation[i:] + permutation[:i]) for i in range(n, 0, -1)]

        if latin_sqr not in latin_sqrs:
            latin_sqrs.append(latin_sqr)

    # Return the list
    return latin_sqrs


def is_latin_square_columns(matrix):
    """
    Verify if a matrix from sympy is a Latin square. This is an auxiliary function for all_square_permutations(n).

    Parameters:
    - matrix (sympy.Matrix): It must not have repetitions of elements in the same row.

    Returns:
    - is_latin_square_columns(matrix): True if it is a Latin square, False otherwise.
    """
    n = matrix.shape[0]

    # Verifies if each number appears only once per column.
    # It is not necessary to verify the rows; permutations do not have repetitions.

    for i in range(0, n):
        for j in range(0, n):
            if matrix.transpose().tolist()[j].count(i+1) != 1:
                return False
    return True


def all_square_permutations(n):
    """
    Generate a the list of all latin squares of order n.

    Parameters:
    - n (int): The order of the matrix and the elements it will contain (1, 2, ..., n).

    Returns:
    - all_square_permutations(n): List of all Latin squares of order n.
    
    Example
    ```python
    cuadrados_latinos = all_square_permutations(3)
    print(cuadrados_latinos)
    ```
    [[Matrix([
     [1, 2, 3],
     [2, 3, 1],
     [3, 1, 2]]),
     Matrix([
     [1, 2, 3],
     [3, 1, 2],
     [2, 3, 1]]),...

    Warning:
    This function may have high time and space complexity for 'n' values larger that 3.
    """
    
    numbers = range(1,n+1)
    latin_sqrs = []
    all_permutations = []
    
    # Generate all permutations, including equivalents
    for permutation in permutations(numbers):
        for i in range(n):
            all_permutations.append(list(permutation[i:] + permutation[:i]))

    for combination in combinations(all_permutations, n):
        # Crea un cuadrado latino al añadir la permutación a sí misma, pero en orden inverso
        latin_sqr = Matrix(list(combination))
        if is_latin_square_columns(latin_sqr) and latin_sqr not in latin_sqrs:
            latin_sqrs.append(latin_sqr)
    return latin_sqrs
