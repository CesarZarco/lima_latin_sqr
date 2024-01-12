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
