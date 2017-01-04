#! /usr/bin/python
# activity_selector
# David Branner
# 20170103

"""Pythonic versions of two illustrations of greedy algorithms.

After Cormen et al. (third edition), Section 16.1.

Here we avoid use of indices and cursors.
"""

from collections import deque

def recursive(lst=None):
    """Identify greedy choice and then recurse on next possible list-tail.
    
    This is not a very interesting recursion.
    """
    # Empty case (not base case)
    if not lst:
        return list()
    # Ensure using deque within `recursive`, to enable popleft
    elif not isinstance(lst, deque):
        lst = deque(lst)

    # Function body begins here.
    greedy_choice = lst.popleft()
    to_return = [greedy_choice]
    while lst:
        if lst[0][0] >= greedy_choice[1]:
            returned = recursive(lst)
            if returned:
                to_return.extend(returned)
        else:
            lst.popleft()
    return to_return

def iterative(lst=None):
    """Add 1st element, greedy choice; iteratively add possible successors."""
    # Empty case
    if not lst:
        return list()

    # Function body begins here.
    to_return = list()
    for item in lst:
        if not to_return:
            to_return = [item] # Initial greedy choice
        elif item[0] >= to_return[-1][1]:
            to_return.append(item)
    return to_return
