from itertools import permutations

def all_square_permutations(n):
    """
    Generate a list of matrices of order N, all of which are Latin squares, using permutations from itertools.

    Parameters:
    - N (int): The order of the matrix and the elements it will contain (1, 2, ..., n).

    Returns:
    - all_square_permutations(N): List of Latin squares that come from permutations as rows.
    
    Example
    cuadrados_latinos = all_square_permutations(3)
    cuadrados_latinos
    [[[1, 2, 3], [2, 3, 1], [3, 1, 2]],
     [[1, 2, 3], [3, 1, 2], [2, 3, 1]],
     [[1, 3, 2], [3, 2, 1], [2, 1, 3]],
     [[1, 3, 2], [2, 1, 3], [3, 2, 1]],
     [[2, 1, 3], [1, 3, 2], [3, 2, 1]],
     [[2, 1, 3], [3, 2, 1], [1, 3, 2]],
     [[2, 3, 1], [3, 1, 2], [1, 2, 3]],
     [[2, 3, 1], [1, 2, 3], [3, 1, 2]],
     [[3, 1, 2], [1, 2, 3], [2, 3, 1]],
     [[3, 1, 2], [2, 3, 1], [1, 2, 3]],
     [[3, 2, 1], [2, 1, 3], [1, 3, 2]],
     [[3, 2, 1], [1, 3, 2], [2, 1, 3]]]
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
