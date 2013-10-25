import pytest
import random
import os
import sys
sys.path.append(os.path.join('..'))
import binary_search_naive as B

def get_random_list():
    random_list = [random.randint(0, 100000) for i in range(1000)]
    return list(set(random_list))

def test_insertion():
    for trial in range(10):
        random_list = get_random_list()
        tree = B.populate_tree(random_list)
        assert B.inorder_traverse(tree) == sorted(random_list)

def test_insertion_including_0():
    random_list = get_random_list()
    random_list.append(0)
    tree = B.populate_tree(random_list)
    assert B.inorder_traverse(tree) == sorted(random_list)

def test_insertion_non_int_keys():
    random_list = get_random_list()
    random_list.append(1.3)
    assert pytest.raises(SystemExit, "B.populate_tree(random_list)")

def test_insertion_dup_keys():
    random_list = get_random_list()
    random_list.append(random_list[-1])
    assert pytest.raises(SystemExit, "B.populate_tree(random_list)")

def test_insert_empty():
    tree = B.populate_tree()
    assert tree == None

def test_inorder_empty():
    tree = B.populate_tree()
    assert B.inorder_traverse(tree) == []

def test_max():
    random_list = get_random_list()
    assert B.max(B.populate_tree(random_list)) == max(random_list)

def test_min():
    random_list = get_random_list()
    assert B.min(B.populate_tree(random_list)) == min(random_list)
