# Import the functions from aux.py
from tilima_square.square_success.sqr_aux import *


SOLUTIONS = []  # List to store the found solutions

def standard_latin_square(square, color):
    """
    Generate standard Latin squares using backtracking.

    This function initiates the generation of a Latin square with a given color.

    Args:
    - square (list): The Latin square under construction.
    - color (int): The current color being placed in the square.

    This function uses backtracking to explore all possible completions of the Latin square.

    Returns:
    - list: List of completed standard Latin squares.
    """
    global SOLUTIONS

    N = len(square)

    for possible_solution in standard_completions(square, color):
        if possible(possible_solution):
            if is_solution(possible_solution):
                SOLUTIONS.append(possible_solution)
            else:
                if completable(possible_solution):
                    if color + 1 <= N:
                        standard_latin_square(possible_solution, color + 1)
    return SOLUTIONS
    
def standard_completions(square, color):
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
        standard_completions_recursive(completions_list, square, color, 1)
        square[0][color-1] = 0

    return completions_list


def standard_completions_recursive(completions_list, square, color, row):
    """
    Recursive function to generate completions for the Latin square.

    Args:
    - completions_list (list): List to store completions.
    - square (list): The Latin square.
    - color (int): The current color being placed in the square.
    - row (int): The current row being processed.

    This function explores all possible completions for a given row and color.
    """
    N = len(square)

    for j in range(N):
        if j == 0:
            if square[color-1][j] == 0:
                square[color-1][j] = color
                if possible(square):
                    if row + 1 < N:
                        standard_completions_recursive(completions_list, square, color, row + 1)
                    else:
                        completions_list.append([row[:] for row in square])
                square[color-1][j] = 0
        else:
            if square[row][j] == 0:
                square[row][j] = color
                if possible(square):
                    if row + 1 < N:
                        standard_completions_recursive(completions_list, square, color, row + 1)
                    else:
                        completions_list.append([row[:] for row in square])
                square[row][j] = 0
