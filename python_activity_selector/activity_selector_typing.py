#! /usr/bin/python
# activity_selector_typing
# David Branner
# 20170104

"""Pythonic versions of two illustrations of greedy algorithms.

After Cormen et al. (third edition), Section 16.1.

Here we avoid use of indices and cursors.

This version using the typing module, which causes Pytest to hang.

Because deques seem to cause trouble when used with typing, I have changed 
back to lists.
"""

import sys
if sys.version_info < (3, 5):
    raise "Python version 3.5 or higher required for 'typing' module."

from typing import List, Tuple, MutableSequence

def recursive(lst: List[Tuple[int, int]]=None) -> List[Tuple[int, int]]:
    """Identify greedy choice and then recurse on next possible list-tail.
    
    This is not a very interesting recursion.
    """
    # Empty case (not base case)
    if not lst:
        return list()

    # Function body begins here.
    greedy_choice = lst.pop(0) # type: Tuple
    to_return = [greedy_choice] # type: List
    while lst:
        if lst[0][0] >= greedy_choice[1]:
            returned = recursive(lst) # type: List
            if returned:
                to_return.extend(returned)
        else:
            lst.pop(0)
    return to_return

def iterative(lst: List[Tuple[int, int]]=None) -> List[Tuple[int, int]]:
    """Add 1st element, greedy choice; iteratively add possible successors."""
    # Empty case
    if not lst:
        return list()

    # Function body begins here.
    to_return = list() # type: List[Tuple[int, int]]
    for item in lst:
        if not to_return:
            to_return = list([item])
        elif item[0] >= to_return[-1][1]:
            to_return.append(item)
    return list(to_return)
