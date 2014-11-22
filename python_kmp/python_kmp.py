#! /usr/bin/env python
# python_kmp.py
# David Prager Branner
# 20141121

"""Implement the Knuth-Morris-Pratt subseq-matching algorithm."""

def fill_skip_ahead_array(subseq):
    """Implement COMPUTE-PREFIX-FUNCTION(P) of Cormen et al., Ch. 32."""
    skip_ahead_array = [0]
    prefix_length = 0
    for element in subseq[1:]:
        while prefix_length and subseq[prefix_length] != element:
            prefix_length = skip_ahead_array[prefix_length - 1]
        if subseq[prefix_length] == element:
            prefix_length += 1
        skip_ahead_array.append(prefix_length)
    return skip_ahead_array

def match(seq, subseq):
    """Implement KMP-MATCHER(T, P) of Cormen et al., Ch. 32, as generator."""
    length = len(subseq)
    if not length:
        return None
    skip_ahead_array = fill_skip_ahead_array(subseq)
    chars_matched = 0
    for cursor, element in enumerate(seq):
        while chars_matched and subseq[chars_matched] != element:
            chars_matched = skip_ahead_array[chars_matched - 1]
        if subseq[chars_matched] == element:
            chars_matched += 1
        if chars_matched == length:
            chars_matched = skip_ahead_array[chars_matched - 1]
            yield cursor - length + 1

