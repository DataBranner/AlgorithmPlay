## Implementation of the Knuth-Morris-Pratt subsequence-matching algorithm

This repository contains a program and a test suite:

    python_kmp.py
    test/test_python_kmp.py

The program `python_kmp.py` contains two functions: 

    match(sequence, subsequence)

This is a generator that returns indexes in the sequence where the matches of the whole subsequence begin. For instance (examples using Ipython v. 2):

    In [1]: import python_kmp as KMP
    
    In [2]: m = KMP.match('abcabc', 'abc')
    
    In [3]: next(m)
    Out[3]: 0
    
    In [4]: next(m)
    Out[4]: 3
    
    In [5]: next(m)
    ---------------------------------------------------------------------------
    StopIteration ...

The `match` function calls another function 

    fill_skip_ahead_array(subsequence)

which returns an array that improves the efficiency of `match` through a clever form of dynamic programming: it reports the longest prefix of the `subsequence` that also appears as a "proper suffix" of `subsequence`. That means the suffix can be skipped in later searches, since it is already known that the suffix is a match for the beginning of the `subsequence`, by some number of characters. 

This implementation basically follows Cormen et al., Ch. 32, with some unobtrusive Pythonic features (zero-indexing, `yield`, `list.append`).

Functions `match` and `fill_skip_ahead_array` are separated to make them easier to write unit tests for. 

[end]