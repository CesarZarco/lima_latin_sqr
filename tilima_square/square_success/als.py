#Import the functions from aux.py, alr.py, alt.py
from tilima_square.square_success.sqr_aux import *

def total_latin_square(square, color):
    
    global SOLUTIONS
    SOLUTIONS = []  # List to store the found solutions
    return total_latin_square2(square, color)

def total_latin_square2(square, color):
    """
    Function to initiate the generation of a Latin square.

    Args:
    - square (list): The Latin square under construction.
    - color (int): The current color being placed in the square.

    This function uses backtracking to explore all possible completions of the Latin square.

    Returns:
    - list: List of all Latin squares without conditions.
    """
    global SOLUTIONS

    N = len(square)

    for possible_solution in completions(square, color):
        if possible(possible_solution):
            if is_solution(possible_solution):
                SOLUTIONS.append(possible_solution)
            else:
                if completable(possible_solution):
                    if color + 1 <= N:
                        total_latin_square2(possible_solution, color + 1)

    return SOLUTIONS

def completions(square, color):
    """
    Generate all possible completions for a row of the Latin square.

    Args:
    - square (list): The Latin square.
    - color (int): The current color being placed in the square.

    Returns:
    - list: List of possible completions for the row.
    """
    completions_list = []
    N = len(square)

    for j in range(N):
        if square[0][j] == 0:
            square[0][j] = color
            completions_recursive(completions_list, square, color, 1)
            square[0][j] = 0

    return completions_list


def completions_recursive(completions_list, square, color, row):
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
        if square[row][j] == 0:
            square[row][j] = color
            if possible(square):
                if row + 1 < N:
                    completions_recursive(completions_list, square, color, row + 1)
                else:
                    completions_list.append([row[:] for row in square])
            square[row][j] = 0
