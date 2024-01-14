# Import functions from sqr_aux.py, list_aux.py and alt.py so that standard_latin_square works
from sqr_aux import *
from list_aux import *
from alt import standard_completions, standard_completions_recursive



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
    for j in range(N-1):
        if list[j] != 0:
            cont[list[j]] += 1
    if any(value > 1 for value in cont.values()):
            return False
    return True
