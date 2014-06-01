# test_linkedlist.py
# David Prager Branner
# 20131119

import pytest
import random
import string
import sys
import os
sys.path.append(os.path.join('..'))
import linkedlist as L

trials = 10
length = 1000

def test_initialize_one_datum():
    for trial in range(trials):
        llist = L.LinkedList(random.random())
        assert llist.length() == 1

def test_initialize_string():
    for trial in range(trials):
        test_string = ''.join([random.choice(string.ascii_letters) for i in
                range(length)])
        llist = L.LinkedList(test_string)
        assert llist.length() == length

def test_initialize_list():
    for trial in range(trials):
        test_list = [random.choice(string.ascii_letters) for i in range(length)]
        llist = L.LinkedList(test_list)
        assert llist.length() == length

def test_return_list():
    for trial in range(trials):
        test_list = [random.choice(string.ascii_letters) for i in range(length)]
        llist = L.LinkedList(test_list)
        assert llist.return_list() == test_list

def test_delete_half_list():
    for trial in range(trials):
        test_list = [random.choice(string.ascii_letters) for i in range(length)]
        llist = L.LinkedList(test_list)
        half_size = len(test_list) // 2
        for counter in range(half_size):
            to_delete = random.choice(test_list)
            llist.delete(to_delete)
            test_list.remove(to_delete)
        assert llist.return_list() == test_list

def test_delete_whole_list():
    for trial in range(trials):
        test_list = [random.choice(string.ascii_letters) for i in range(length)]
        llist = L.LinkedList(test_list)
        size = len(test_list)
        for counter in range(size):
            to_delete = random.choice(test_list)
            llist.delete(to_delete)
            test_list.remove(to_delete)
        # how do you test the raising of an error here?
        pytest.raises(AttributeError, 'llist.root')
