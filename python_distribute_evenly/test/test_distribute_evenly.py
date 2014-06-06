# test_distribute_evenly.py
# David Prager Branner
# 20140606

import distribute_evenly as D

def test_01():
    string_of_lines = (
            '''1 3 4\n'''
            '''1 2 3\n'''
            '''1 3\n'''
            '''1 4 2''')
    expected_output = ['2 2 1', '4 1 2', '2 2 3', '4 1 3', '3 1 4']
    assert D.main(string_of_lines) == expected_output
    
def test_02():
    string_of_lines = (
            '''2 1 2\n'''
            '''2 2 1''')
    expected_output = []
    assert D.main(string_of_lines) == expected_output
    
def test_03():
    string_of_lines = (
            '''1 3 4 5 7\n'''
            '''1 3\n'''
            '''2''')
    expected_output = ['2 3 1',
            '2 3 2',
            '4 1 2',
            '5 1 2',
            '7 1 2',
            '1 1 3',
            '3 1 3',
            '4 1 3',
            '5 1 3',
            '7 1 3']
    assert D.main(string_of_lines) == expected_output

# Further tests: use the output to update contents of `collections` and 
# then see if all collections are complete.