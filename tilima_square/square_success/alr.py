# Import the functions from aux.py
from sqr_aux import *
from als import completions_recursive

def reduced_latin_square(square, color):
    """
    Function to initiate the generation of a Latin square.

    Args:
    - square (list): The Latin square under construction.
    - color (int): The current color being placed in the square.

    This function uses backtracking to explore all possible completions of the Latin square.
    
    Returns:
    - list: List of completed reduced Latin squares.
    """
    global SOLUTIONS

    N = len(square)

    for possible_solution in reduced_completions(square, color):
        if possible(possible_solution):
            if is_solution(possible_solution):
                SOLUTIONS.append(possible_solution)
            else:
                if completable(possible_solution):
                    if color + 1 <= N:
                        reduced_latin_square(possible_solution, color + 1)
    return SOLUTIONS

def reduced_completions(square, color):
    """
    Generate all possible completions for a row of the Latin square.

    Args:
    - square (list): The Latin square.
    - color (int): The current color being placed in the square.

    Returns:
    - list: List of possible completions for the row.
    """
    completions_list = []

    if square[0][color-1] == 0:
        square[0][color-1] = color
        completions_recursive(completions_list, square, color, 1)
        square[0][color-1] = 0

    return completions_list
