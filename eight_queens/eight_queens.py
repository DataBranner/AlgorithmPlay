# eight_queens.py
# David Prager Branner
# 20140718

import random

def solve(accepted=None, still_available=None, cols=8, rows=8):
    # Base case.
    if not (cols or rows):
        return accepted
    #
    # Recursive block
    if accepted is None:
        accepted = []
    # Populate all possible cells in list-of-sets still_available.
    # We count columns top to bottom, rows left to right.
    if still_available is None:
        still_available = [set()]
        still_available.extend([set(column for column in range(cols))
                    for row in range(rows-1)])
    # Choose random first queen.
    accepted.append(random.randint(0, cols-1))
    eliminate_reachables(accepted[0], 0, still_available)
    # Eliminate cells reachable from newest queen.
    for row in range(1, rows):
        # QQQ How do we backtrack if the first column is no good?
        for column in still_available[row]:
            accepted.append(column)
        still_available = eliminate_reachables(column, row, still_available)
    return accepted

def eliminate_reachables(column, row, still_available):
    for r in range(row+1, len(still_available)):
        # Same column.
        if column in r:
            still_available[r].remove(column)
        # Diagonals.
        for reachable in [r - row, r + row]:
            if reachable >= 0 and reachable in still_available[r]:
                print('row {} before: {}'.
                        format(row, still_available[r]), end=' ')
                still_available[r].remove(reachable)
                print('after: {}'.format(still_available[r]))
    return still_available
