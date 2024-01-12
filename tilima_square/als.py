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

def latin_square(square, color):
    """
    Main function to print the Latin squares.

    Args:
    - N (int): Order of the Latin squares required.

    This function only calls latin_square to show results
    """
    
    global SOLUTIONS
    square = [[0 for _ in range(N)] for _ in range(N)]
    
    if not isinstance(N, int) or N <= 0:
        raise ValueError("N must be a positive integer.")
    
    if N == 1:
        print(f'Total solutions found: 1')
        print(f'Solutions found: [1]')
    else:
        if type == 'TOTAL':
            print(f'Total solutions found: {len(total_latin_square(square,1))}')
            print(f'Solutions found: ')
            for solution in SOLUTIONS:
                print(solution)

        if type == 'REDUCED':
            print(f'Total solutions found: {len(reduced_latin_square(square,1))}')
            print(f'Solutions found: ')
            for solution in SOLUTIONS:
                print(solution)

        if type == 'STANDARD':
            print(f'Total solutions found: {len(standard_latin_square(square,1))}')
            print(f'Solutions found: ')
            for solution in SOLUTIONS:
                print(solution)
    # Return to 0 de values
    SOLUTIONS = []
