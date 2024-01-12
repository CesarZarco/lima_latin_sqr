#Import all auxiliar files
from als import *
from alr import *
from alt import *

SOLUTIONS = []
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
