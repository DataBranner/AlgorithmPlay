#! /usr/bin/python
# test_activity_selector_typing
# David Branner
# 20170103

"""Supply tests (with one utility function)."""

from collections import deque
from operator import itemgetter
import os
import sys
sys.path.append(os.path.join('..', 'activity_selector'))
from typing import List, Tuple

import activity_selector_typing as AS

def sort_by_final_value(lst: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """Provide utility sort by index 1"""
    return sorted(lst, key=itemgetter(1))



def test_recursive_four_items() -> None:
    """Test four item case recursively."""
    activities = deque([(1, 5), (2, 4), (3, 7), (2, 3)])
    activities = sort_by_final_value(activities)
    expected = deque([(2, 3), (3, 7)])
    observed = AS.recursive(activities)
    assert observed == expected

def test_recursive_one_item() -> None:
    """Test single item recursively."""
    activities = deque([(4, 7)])
    activities = sort_by_final_value(activities)
    expected = deque([(4, 7)])
    observed = AS.recursive(activities)
    assert observed == expected

def test_recursive_empty_case() -> None:
    """Test empty list recursively."""
    activities = deque()
    activities = sort_by_final_value(activities)
    expected = deque()
    observed = AS.recursive(activities)
    assert observed == expected

def test_recursive_cormen_example() -> None:
    """Test example from Cormen volume recursively."""
    activities = [(1, 4),  (3, 5),  (0, 6),  (5, 7),  (3, 9), (5, 9),
                  (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    activities = sort_by_final_value(activities)
    expected = deque([(1, 4), (5, 7), (8, 11), (12, 16)])
    observed = AS.recursive(activities)
    assert observed == expected

def test_iterative_four_items() -> None:
    """Test four item case iteratively."""
    activities = deque([(1, 5), (2, 4), (3, 7), (2, 3)])
    activities = sort_by_final_value(activities)
    expected = deque([(2, 3), (3, 7)])
    observed = AS.iterative(activities)
    assert observed == expected

def test_iterative_one_item() -> None:
    """Test single item iteratively."""
    activities = deque([(4, 7)])
    activities = sort_by_final_value(activities)
    expected = deque([(4, 7)])
    observed = AS.iterative(activities)
    assert observed == expected

def test_iterative_empty_case() -> None:
    """Test empty list iteratively."""
    activities = deque()
    activities = sort_by_final_value(activities)
    expected = deque()
    observed = AS.iterative(activities)
    assert observed == expected

def test_iterative_cormen_example() -> None:
    """Test example from Cormen volume iteratively."""
    activities = [(1, 4),  (3, 5),  (0, 6),  (5, 7),  (3, 9), (5, 9),
                  (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    activities = sort_by_final_value(activities)
    expected = deque([(1, 4), (5, 7), (8, 11), (12, 16)])
    observed = AS.iterative(activities)
    assert observed == expected

