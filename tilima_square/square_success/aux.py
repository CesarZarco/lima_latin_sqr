def is_solution(square):
    """
    Check if a given square is a complete Latin square.

    Args:
    - square (list): The Latin square.

    Returns:
    - bool: True if the square is a complete Latin square, False otherwise.
    """
    return not completable(square)


def completable(square):
    """
    Check if it is possible to complete the square with at least one empty cell.

    Args:
    - square (list): The Latin square.

    Returns:
    - bool: True if the square is completable, False otherwise.
    """
    N = len(square)

    for i in range(N):
        for j in range(N):
            if square[i][j] == 0:
                return True
    return False


def possible(square):
    """
    Check if the partial Latin square is a valid Latin square.

    Args:
    - square (list): The Latin square.

    Returns:
    - bool: True if the square is a valid Latin square, False otherwise.
    """
    N = len(square)
    
    for i in range(N):
        # Check columns
        cont = {x: 0 for x in range(1, N + 1)}
        for j in range(N):
            if square[j][i] != 0:
                cont[square[j][i]] += 1
        if any(value > 1 for value in cont.values()):
            return False

        # Check rows
        cont = {x: 0 for x in range(1, N + 1)}
        for j in range(N):
            if square[i][j] != 0:
                cont[square[i][j]] += 1
        if any(value > 1 for value in cont.values()):
            return False

    return True
