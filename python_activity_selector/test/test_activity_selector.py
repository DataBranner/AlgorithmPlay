#! /usr/bin/python
# test_activity_selector
# David Branner
# 20170103

"""Supply tests (with one utility function)."""

from operator import itemgetter
import os
import sys
sys.path.append(os.path.join('..', 'activity_selector'))

import activity_selector as AS

def sort_by_final_value(lst):
    """Provide utility sort by index 1"""
    return sorted(lst, key=itemgetter(1))



def test_recursive_four_items():
    """Test four item case recursively."""
    activities = [(1, 5), (2, 4), (3, 7), (2, 3)]
    activities = sort_by_final_value(activities)
    expected = [(2, 3), (3, 7)]
    observed = AS.recursive(activities)
    assert observed == expected

def test_recursive_one_item():
    """Test single item recursively."""
    activities = [(4, 7)]
    activities = sort_by_final_value(activities)
    expected = [(4, 7)]
    observed = AS.recursive(activities)
    assert observed == expected

def test_recursive_empty_case():
    """Test empty list recursively."""
    activities = []
    activities = sort_by_final_value(activities)
    expected = list()
    observed = AS.recursive(activities)
    assert observed == expected

def test_recursive_cormen_example():
    """Test example from Cormen volume recursively."""
    activities = [(1, 4),  (3, 5),  (0, 6),  (5, 7),  (3, 9), (5, 9),
                  (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    activities = sort_by_final_value(activities)
    expected = [(1, 4), (5, 7), (8, 11), (12, 16)]
    observed = AS.recursive(activities)
    assert observed == expected

def test_iterative_four_items():
    """Test four item case iteratively."""
    activities = [(1, 5), (2, 4), (3, 7), (2, 3)]
    activities = sort_by_final_value(activities)
    expected = [(2, 3), (3, 7)]
    observed = AS.iterative(activities)
    assert observed == expected

def test_iterative_one_item():
    """Test single item iteratively."""
    activities = [(4, 7)]
    activities = sort_by_final_value(activities)
    expected = [(4, 7)]
    observed = AS.iterative(activities)
    assert observed == expected

def test_iterative_empty_case():
    """Test empty list iteratively."""
    activities = []
    activities = sort_by_final_value(activities)
    expected = list()
    observed = AS.iterative(activities)
    assert observed == expected

def test_iterative_cormen_example():
    """Test example from Cormen volume iteratively."""
    activities = [(1, 4),  (3, 5),  (0, 6),  (5, 7),  (3, 9), (5, 9),
                  (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    activities = sort_by_final_value(activities)
    expected = [(1, 4), (5, 7), (8, 11), (12, 16)]
    observed = AS.iterative(activities)
    assert observed == expected

