from itertools import permutations, combinations

def square_0(N):
    """
    This function is a simple utility for creating zero-filled square matrices of a specified order N.

    Parameters:
    - N (int): The order of the square matrix required.

    Returns:
    - square_0(N): List of order N, which elements are all lists of order N with zeros.
    """
    return [[0 for _ in range(N)] for _ in range(N)]
