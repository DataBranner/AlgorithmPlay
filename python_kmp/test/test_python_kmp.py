# test_python_kmp.py
# 20141120

import sys
sys.path.append('..')
import python_kmp as KMP
import random
import string
import re

# For testing our results we use a different version of the 
# COMPUTE-PREFIX-FUNCTION for KMP, by Keith Schwarz.
# http://www.keithschwarz.com/interesting/code/knuth-morris-pratt/KnuthMorrisPratt.python.html
# Accessed 20141120.
def failTable(pattern):
    # Create the resulting table, which for length zero is None.
    result = [None]
    # Iterate across the rest of the characters, filling in the values for the
    # rest of the table.
    for i in range(0, len(pattern)):
        # Keep track of the size of the subproblem we're dealing with, which
        # starts off using the first i characters of the string.
        j = i
        while True:
            # If j hits zero, the recursion says that the resulting value is
            # zero since we're looking for the LPB of a single-character
            # string.
            if j == 0:
                result.append(0)
                break
            # Otherwise, if the character one step after the LPB matches the
            # next character in the sequence, then we can extend the LPB by one
            # character to get an LPB for the whole sequence.
            if pattern[result[j]] == pattern[i]:
                result.append(result[j] + 1)
                break
            # Finally, if neither of these hold, then we need to reduce the
            # subproblem to the LPB of the LPB.
            j = result[j]
    return result

def random_string(length=100, chars=4):
    inventory = random.sample(string.ascii_letters, chars)
    return ''.join(random.choice(inventory) for _ in range(length))

def test_fill_skip_ahead_array_01():
    assert KMP.fill_skip_ahead_array('abcde') == [0, 0, 0, 0, 0]

def test_fill_skip_ahead_array_02():
    assert KMP.fill_skip_ahead_array('aaaaa') == [0, 1, 2, 3, 4]

def test_fill_skip_ahead_array_03():
    assert KMP.fill_skip_ahead_array('aaabaaa') == [0, 1, 2, 0, 1, 2, 3]

def test_fill_skip_ahead_array_04():
    assert KMP.fill_skip_ahead_array(
            'aaacaaaaac') == [ 0, 1, 2, 0, 1, 2, 3, 3, 3, 4]

def test_fill_skip_ahead_array_05():
    assert KMP.fill_skip_ahead_array('ababaca') == [0, 0, 1, 2, 3, 0, 1]

def test_fill_skip_ahead_array_06():
    assert KMP.fill_skip_ahead_array('ababacababab') == [
            0, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 4]

def test_fill_skip_ahead_array_07():
    """Test random subsequence against failTable results."""
    for i in range(100):
        rand_str = random_string()
        assert KMP.fill_skip_ahead_array(rand_str) == failTable(rand_str)[1:]

def test_fill_skip_ahead_array_08():
    """Test random subsequence against failTable results."""
    for i in range(100):
        rand_str = random_string(10, 7)
        assert KMP.fill_skip_ahead_array(rand_str) == failTable(rand_str)[1:]

def test_fill_skip_ahead_array_09():
    """Test random subsequence against failTable results."""
    for i in range(100):
        rand_str = random_string(20, 40)
        assert KMP.fill_skip_ahead_array(rand_str) == failTable(rand_str)[1:]

def test_fill_skip_ahead_array_10():
    """Test empty subsequence."""
    assert KMP.fill_skip_ahead_array('') == [0]

def test_fill_skip_ahead_array_11():
    """Test subsequence without repetitions."""
    assert KMP.fill_skip_ahead_array(['a', 'c']) == [0, 0]

def test_fill_skip_ahead_array_12():
    """Test subsequence with simple-case repetition."""
    assert KMP.fill_skip_ahead_array(['a', 'c', 'a', 'c']) == [0, 0, 1, 2]

def test_match_01():
    assert list(KMP.match('abcdabcdabceabcd', 'abcd')) == [0, 4, 12]

def test_match_02():
    assert list(KMP.match('abcdabcdabceabcd', 'abc')) == [0, 4, 8, 12]

def test_match_03():
    """Test empty subsequence."""
    assert list(KMP.match('abcdabcdabceabcd', '')) == []

def test_match_04():
    """Test random sequence against re.finditer results."""
    for _ in range(100):
        seq = random_string(1000, 3)
        subseq = seq[-4:]
        print(seq, subseq)
        assert list(KMP.match(seq, subseq)) == [
                i.start() for i in re.finditer('(?='+subseq+')', seq)]
