# test_solve_eight_queens.py
# David Prager Branner
# 20140718

import eight_queens

cols = 8
rows = 8
array = eight_queens.solve(cols=8, rows=8)

def test_size(array):
    assert len(array) == 8

def test_horizontals(array):
    horizontals = [item[0] for item in array]
    assert list(set(horizontals)) == horizontals

def test_verticals(array):
    verticals = [item[1] for item in array]
    assert list(set(verticals)) == verticals

def test_diags(array):
    array.sort()
    for first, second in zip(array, array[1:]):
        # Compare jump between each index of each successive element
        assert second[1] - first[1] != second[0] - first[0]
