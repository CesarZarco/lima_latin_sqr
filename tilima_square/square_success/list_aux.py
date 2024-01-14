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

def generate_combinations(elements, length, current=None):
    """
    Generate all possible combinations of a list without repetitions.

    Parameters:
    - elements (list): The list of elements to generate combinations from.
    - length (int): The length of each combination.
    - current (list): Internal parameter for recursion. Keeps track of the current combination being generated.

    Returns:
    - list: A list of all possible combinations.
    """
    if current is None:
        current = []

    if length == 0:
        yield current
        return
    
    elements_list = list(elements)  # Convert the generator to a list
    for i, element in enumerate(elements_list):
        remaining_elements = elements_list[i + 1:]
        yield from generate_combinations(remaining_elements, length - 1, current + [element])
