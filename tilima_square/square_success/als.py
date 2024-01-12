#Import the functions from aux.py, alr.py, alt.py
from aux import completions, possible, is_solution, completable, 
from alr import reduced_latin_square 
from alt import standard_latin_square

SOLUTIONS = []  # List to store the found solutions

def total_latin_square(N):
    """
    Main function to initiate the generation of a Latin square.

    Args:
    - square (list): The Latin square under construction.
    - color (int): The current color being placed in the square.

    This function uses backtracking to explore all possible completions of the Latin square.
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
                        total_latin_square(possible_solution, color + 1)

    return SOLUTIONS
