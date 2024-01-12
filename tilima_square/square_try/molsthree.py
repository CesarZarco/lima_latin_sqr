def check_orthogonality(square_list):
    """
    Checks the orthogonality of a list of 3x3 Latin squares, since to verify that two squares are MOLS, n-1 elements are taken per entry.

    Arguments:
    - square_list (list): List of Latin squares whose orthogonality must be checked.

    This function checks the orthogonality of pairs of Latin squares in the given list.
    Iterate through all the pairs and check if they are orthogonal.

    Print the result, indicating whether at least one pair of Latin squares is orthogonal.
    If there are orthogonal pairs, it also prints the total number of orthogonal pairs.

    Note: This function assumes that Latin squares are represented as lists of lists.

    Example usage:
    check_orthogonality(SOLUTIONS)
    
    """
    n = len(square_list[0])
    orthogonal_pairs = []
    total_pairs = 0

    for h in range(len(square_list)):
        for i in range(h, len(square_list)):
            unique_elements = set()
            
            for j in range(len(square_list[i])):
                for k in range(len(square_list[i][j])):
                    if (square_list[h][j][k], square_list[i][j][k]) not in unique_elements:
                        unique_elements.add((square_list[h][j][k], square_list[i][j][k]))
                    else:
                        break
            
                if (square_list[h], square_list[i]) not in orthogonal_pairs and len(unique_elements) == n**2:
                    orthogonal_pairs.append((Matrix(square_list[i]), Matrix(square_list[h])))
                    total_pairs = len(orthogonal_pairs)

    if len(orthogonal_pairs) == 0:
        print("No pair of Latin squares is orthogonal.")
    else:
        print(f"At least one pair of Latin squares is orthogonal, total pairs: {total_pairs}")
        # Uncomment the line below if you want to return the list of orthogonal pairs
        # return orthogonal_pairs
