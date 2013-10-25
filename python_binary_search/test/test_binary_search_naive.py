import pytest
import random
import os
import sys
sys.path.append(os.path.join('..'))
import binary_search_naive as B

def get_random_list_unique(size=1000):
    random_list = [random.randint(0, 100000) for i in range(size)]
    return list(set(random_list))

def test_insertion():
    for trial in range(10):
        random_keys = get_random_list_unique()
        tree = B.populate_tree(random_keys)
        assert B.inorder_traverse(tree) == sorted(random_keys)

def test_insertion_including_0():
    random_keys = get_random_list_unique()
    random_keys.append(0)
    tree = B.populate_tree(random_keys)
    assert B.inorder_traverse(tree) == sorted(random_keys)

def test_insertion_non_int_keys():
    random_keys = get_random_list_unique()
    random_keys.append(1.3)
    assert pytest.raises(SystemExit, "B.populate_tree(random_keys)")

def test_insertion_dup_keys():
    random_keys = get_random_list_unique()
    random_keys.append(random_keys[-1])
    assert pytest.raises(SystemExit, "B.populate_tree(random_keys)")

def test_keys_diff_number_data():
    random_keys = get_random_list_unique(1000)
    random_data = get_random_list_unique(500)
    assert pytest.raises(SystemExit, 
            "B.populate_tree(random_keys, random_data)")

def test_insert_empty():
    tree = B.populate_tree()
    assert tree == None

def test_inorder_empty():
    tree = B.populate_tree()
    assert B.inorder_traverse(tree) == []

def test_max():
    random_keys = get_random_list_unique()
    assert B.max(B.populate_tree(random_keys)) == max(random_keys)

def test_min():
    random_keys = get_random_list_unique()
    assert B.min(B.populate_tree(random_keys)) == min(random_keys)
