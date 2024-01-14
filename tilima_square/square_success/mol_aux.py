# Import functions from sqr_aux.py and alt.py so that standard_latin_square works
from sqr_aux import *
from alt import standard_completions, standard_completions_recursive

def generate_permutations(elements):
    """
    Generate all permutations of a list of elements.

    Parameters:
    - elements (list): The list of elements to generate permutations from.

    Returns:
    - list of lists: A list containing all permutations of the input elements.
      Each permutation is represented as a list.
    """
    if len(elements) == 0:
        # Base case: an empty list has one permutation, an empty list.
        return [[]]

    permutations = []
    for i in range(len(elements)):
        # Select the current element and exclude it from the remaining elements.
        current_element = elements[i]
        remaining_elements = elements[:i] + elements[i + 1:]

        # Recursively generate permutations for the remaining elements.
        for p in generate_permutations(remaining_elements):
            # Combine the current element with each permutation of the remaining elements.
            permutations.append([current_element] + p)

    return permutations

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


