#! /usr/bin/env python
# python_kmp.py
# David Prager Branner
# 20141120

"""Implement the Knuth-Morris-Pratt subsequence-matching algorithm."""

def fill_skip_ahead_array(subsequence):
    """Implement COMPUTE-PREFIX-FUNCTION(P) of Cormen et al., Ch. 32."""
    skip_ahead_array = [0]
    prefix_length = 0
    for cursor, element in enumerate(subsequence[1:]):
        while prefix_length and subsequence[prefix_length] != element:
            prefix_length = skip_ahead_array[prefix_length - 1]
        if subsequence[prefix_length] == element:
            prefix_length += 1
        skip_ahead_array.append(prefix_length)
    return skip_ahead_array

def match(sequence, subsequence):
    """Implement KMP-MATCHER(T, P) of Cormen et al., Ch. 32, as generator."""
    length = len(subsequence)
    if not length:
        return None
    skip_ahead_array = fill_skip_ahead_array(subsequence)
    chars_matched = 0
    for cursor, element in enumerate(sequence):
        while chars_matched and subsequence[chars_matched] != element:
            chars_matched = skip_ahead_array[chars_matched - 1]
        if subsequence[chars_matched] == element:
            chars_matched += 1
        if chars_matched == length:
            chars_matched = skip_ahead_array[chars_matched - 1]
            yield cursor - length + 1

