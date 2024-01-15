#Import all auxiliar files
from tilima_square.square_success.als import *
from tilima_square.square_success.alr import *
from tilima_square.square_success.alt import *
from tilima_square.square_success.mol_aux import *

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

def mols(N):
    
    """
    Main function, calls mols and prints results while the user says yes.

    Parameters:
        N (int): Order of the MOLS to be shown.
    """
    
    if not isinstance(N, int) or N <= 1:
        raise ValueError("N must be a positive integer greater that 1.")
    
    combinations = mols_generator(N) 
    while True:
    # Tu código aquí
        squares = next(combinations)
        all = []
        for square in squares:
            all.append([row[:] for row in square])
        print(all)
            
    
        answer = input("Would you like another? (y/n): ").lower()
    
        if answer != 'y':
            break  # leave oherwise
