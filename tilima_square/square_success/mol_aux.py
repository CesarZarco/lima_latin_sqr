# Import functions from sqr_aux.py, list_aux.py and alt.py so that standard_latin_square works
from tilima_square.square_success.sqr_aux import *
from tilima_square.square_success.list_aux import *
from tilima_square.square_success.alt import standard_completions, standard_completions_recursive



def standard_generator(square, color):
    """
    Function to initiate the generation of a Latin square in its standard form.

    Args:
    - square (list): The Latin square under construction.
    - color (int): The current color being placed in the square.

    This function uses backtracking to explore all possible completions of the Latin square.
    """

    N = len(square)

    for possible_solution in standard_completions(square, color):
        if possible(possible_solution):
            if is_solution(possible_solution):
                yield possible_solution
            else:
                if completable(possible_solution):
                    if color + 1 <= N:
                        yield from standard_generator(possible_solution, color + 1)

def reduced_generator(standardized,N):
    """
    Generate reduced Latin squares by permutating rows of standardized Latin squares.

    Args:
    - standarized (list): The list of standardized Latin squares.

    This function permutes rows of a standardized Latin square to explore all possible completions of the reduced Latin square.
    """
    
    for standard in standardized:
        reduced = []
        
        # Generate new square to complete
        square = [[0 for _ in range(N)] for _ in range(N)]
        for j in range(N):
            square[0][j] = j + 1
        # Complete a new square with each permutation
        for permutation in generate_permutations(standard[1:]):
            for i in range(len(permutation)):
                for j in range(N):
                    square[i + 1][j] = permutation[i][j]
            reduced.append([row[:] for row in square])
        yield reduced


def useful(list, N):
    """
    Check if a list represents a useful configuration.

    Args:
    - lst (list): The input list to be checked.

    Returns:
    - bool: True if the input list represents a useful configuration, False otherwise.

    This function checks the input list for useful properties:
    1. It verifies that each element in the list appears at most once.
    2. If an element appears more than once, the function returns False, indicating the configuration is not useful.
    3. If all elements appear at most once, the function returns True, indicating a useful configuration.
    """
    
    # Check list
    cont = {x: 0 for x in range(1, N + 1)}
    
    # Count occurrences of each element in the list
    for j in range(N-1):
        if list[j] != 0:
            cont[list[j]] += 1
    # Check if any element appears more than once
    if any(value > 1 for value in cont.values()):
            return False
    return True

def usable(list_squares, aux, i, j):
    """
    Checks if an auxiliary list (represented by 'aux') can be placed at position (i, j)
    in the list of squares (represented by 'list_squares') without violating the game rules.

    Parameters:
    - list_squares (list): A 3D matrix of squares represented as a list of lists of lists.
    - aux (list): Auxiliary list being attempted to be placed at position (i, j).
    - i (int): Row index where the auxiliary square is being attempted to be placed.
    - j (int): Column index where the auxiliary square is being attempted to be placed.

    Returns:
    - bool: True if the auxiliary square can be placed at position (i, j) without violating the rules,
             False otherwise.
    """
    N = len(list_squares[0])  # Order of each square
    M = len(list_squares)     # Number of squares in the list

    # Iterate over the list of squares 
    for m in range(0, M-1):
        # Iterate over the rows in the matrix (up to the first-to-last row)
        for k in range(1, N):
            # Iterate over the columns in each square
            for l in range(N):
                # Ignore the current position (i, j)
                if i == k and j == l:
                    continue

                # Compare the sub-list of 'aux' with the sub-list of the matrix at position (k, l)
                if aux[m:m+2] == aux_list(list_squares, k, l)[m:m+2]:
                    return False  # If there is a match, the auxiliary square cannot be placed

    return True  # If no matches are found, the auxiliary square can be placed at position (i, j)


def aux_list(list_squares, i, j):
    """
    Returns a list representing the sub-list of the matrix 'list_squares'
    at position (i, j) across all squares.

    Parameters:
    - list_squares (list): A 3D matrix of squares represented as a list of lists of lists.
    - i (int): Row index within each square.
    - j (int): Column index within each square.

    Returns:
    - list: Sub-list of the matrix at position (i, j) across all squares.
    """
    M = len(list_squares)            # Number of squares in the matrix
    aux = [0 for _ in range(M)]      # Initialize an auxiliary list

    # Extract the element at position (i, j) from each square and store it in the auxiliary list
    for k in range(M):
        aux[k] = list_squares[k][i][j]

    return aux

def are_orthogonal(list_squares):
    """
    Check if a list of reduced latin squares satisfies certain orthogonality conditions 
    based on orthogonality in Latin squares.

    Parameters:
    - list_squares (list): A list of squares represented as a 2D list.

    Returns:
    - bool: True if the list of squares is orthogonal, False otherwise. 
    """

    # Get the size of the squares (assuming all squares have the same size)
    N = len(list_squares[0])

    # Iterate through each pair of squares
    for i in range(1, N):
        for j in range(N):
            # Get auxiliary information using aux_list function
            aux = aux_list(list_squares, i, j)

            # Check if the auxiliary information is useful using the useful function
            if not useful(aux, N):
                return False

            # Check if the current square and its auxiliary information are usable
            if not usable(list_squares, aux, i, j):
                return False

    # If all pairs satisfy the conditions, return True
    return True

def mols_generator(N):
    """
    Generate combinations of squares that are MOLS.

    Parameters:
    - N (int): Order of the MOLS to be construct.

    Yields:
    - List[List[int]]: Each yielded combination is a list of N-1 vectors, where each vector is represented as a list of integers.

    The function uses standard_generator, reduced_generator, generate_combinations, and are_orthogonal functions to generate and filter combinations based on specific criteria.
    """
    # Create an empty square matrix of size N x N
    square = [[0 for _ in range(N)] for _ in range(N)]

    # Generate a standardized square matrix with specific properties
    standarized = standard_generator(square, 1)
    permutations = reduced_generator(standarized, N)
    for permutation in permutations:
        # Check if the vectors in the combination are orthogonal
        combinations = generate_combinations(permutation, N-1)
        for combination in combinations:
            if are_orthogonal(combination):
                yield combination
                
    print("is all")
    return None
