import numpy as np

def standard_matrix(n):
    """
    Generate a matrix of order n in its standard form.

    The standard form of the matrix is a zeros matrix with the first row
    and the first column containing natural numbers from 1 to n in increasing order.

    Parameters:
    - n (int): The order of the matrix and the maximum value for the elements in the
              first row and column (1, 2, ..., n).

    Returns:
    - np.ndarray: Matrix in its standard form represented by a NumPy array.

    Example:
    >>> standard_matrix(3)
    array([[1, 2, 3],
           [1, 0, 0],
           [2, 0, 0]])

    Raises:
    - ValueError: If n is not a positive integer.
    """

    # Validate input
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer.")

    # Create a zeros matrix
    S = np.zeros((n, n), dtype=int)
    
    # Initialize the first row and column
    S[0, :] = np.arange(1, n + 1)
    S[:, 0] = np.arange(1, n + 1)

    return S

