import pytest
import random
import os
import sys
sys.path.append(os.path.join('..'))
import binary_search_naive as B

def test_insertion():
    for trial in range(10):
        random_integers = [random.randint(0, 100000) for i in range(1000)]
        tree = B.populate_tree(random_integers)
        assert B.inorder_traverse(tree) == sorted(random_integers)
