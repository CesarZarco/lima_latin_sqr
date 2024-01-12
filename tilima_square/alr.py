# Import the functions from aux.py
from aux import reduced_completions, possible, is_solution, completable

def reduced_latin_square(square, color):
    """
    Main function to initiate the generation of a Latin square.

    Args:
    - square (list): The Latin square under construction.
    - color (int): The current color being placed in the square.

    This function uses backtracking to explore all possible completions of the Latin square.
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
