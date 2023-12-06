from itertools import permutations, combinations
from sympy import Matrix, init_printing
init_printing(use_latex=True)

def inicial(n):
    for i in range(1,n+1):
        if i == 1:
            M = [list((range(1,n+1)))]
        else:
            S = [0]*n
            S[0] = i
            M.append(S)
    return M
