# Recurrencia
# -----------
#  t(n,w) = 0                                    : if n <= 0 or w = 0
#         = t(n-1,w)                             : if w(n) > w
#         = max (t(n-1,w), t(n-1,w-w(n)) + B(n))

import numpy as np

def solve_tabulation(items, capacity):
    taken = []
    table = np.zeros((len(items)+1,capacity+1), dtype=int)

    def fill_table():
        for x in range(1, n+1):
            for y in range(w+1):
                if items[x - 1].weight <= y:
                    if items[x - 1].value + table[x - 1][y - items[x - 1].weight] > table[x - 1][y]:
                        table[x][y] = items[x - 1].value + table[x - 1][y - items[x - 1].weight]
                    else:
                        table[x][y] = table[x - 1][y]
                else:
                    table[x][y] = table[x - 1][y]
        return

    def fill_taken(n, w):

        taken_copy = [0] * n
        n_copy = n
        w_copy = w
        while n_copy > 0 and w_copy > 0:
            if table[n_copy][w_copy] != table[n_copy - 1][w_copy]:
                taken_copy[n_copy - 1] = items[n_copy-1].index
                n_copy -= 1
                w_copy -= items[n_copy].weight
            else:
                n_copy -= 1

        for i in reversed(taken_copy):
            if i!=0:
                taken.insert(0, i)
        return

    n=len(items)
    w=capacity
    
    fill_table()                # Relleno la tabla
    fill_taken(n,w)             # Genero la lista de items elegidos

    return table[-1][w], taken
