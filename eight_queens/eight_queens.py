# eight_queens.py
# David Prager Branner
# 20140718

def solve(accepted=None, still_to_test=None, cols=8, rows=8):
    # Base case.
    if not (cols or rows):
        return accepted
    #
    # Recursive block
    if accepted is None:
        accepted = []
    # Populate all possible cells in still_to_test.
    if still_to_test is None:
        still_to_test = {(column, row)
                for column in range(cols)
                for row in range(rows)}
    # Eliminate cells reachable from newest queen.
    for column in still_to_test:
        for row in column:
            cell_to_try = (column, row)
            pass
