# test_hash_tables.py
# 20130915
# David Prager Branner

'''Test suite for Python implementation of a hash table with chaining and
resizing.'''

import os
import sys
import random
import string
sys.path.append(os.path.join('..'))
import hash_table

def random_key(the_range=8): 
    '''Generate string of random ASCII letters for use as random key.'''
    return ''.join([random.choice(string.ascii_letters) 
            for i in range(the_range)])

# Fill dictionary with random keys and values.
dictionary = {random_key() : random.randint(-1000, 1000) for i in range(1000)}

def test_create():
    '''Test creation of hash table of various sizes.'''
    for trial in range(10):
        size = random.randint(4, 64)
        ht = hash_table.Hash_Table(size)
        assert ht.size == size

def test_insert_retrieve():
    '''Test retrieval of inserted items.'''
    size = 16
    ht = hash_table.Hash_Table(size)
    # Use dictionary to populate hash table.
    _ = [ht.insert(item, dictionary[item]) for item in dictionary]
    # Test by comparing individual items.
    for trial in range(25):
        test_key = random.sample(dictionary.keys(), 1)[0]
        assert ht.retrieve(test_key) == dictionary[test_key]

def test_collisions_cause_chaining():
    '''Test whether collisions lead to the presence of a list in the slot in
    question, rather than a plain string value.'''
    ht = hash_table.Hash_Table(1)
    for insertion in range(5):
        test_key = random.sample(dictionary.keys(), 1)[0]
        ht.insert(test_key, dictionary[test_key])
    assert isinstance(ht.array[0], list)

def test_nothing_added_twice():
    '''Test whether anything is added twice.'''
    ht = hash_table.Hash_Table(1)
    test_key = random.sample(dictionary.keys(), 1)[0]
    for i in range(2):
        ht.insert(test_key, dictionary[test_key])
    assert not isinstance(ht.array[0], list)

def test_resizing():
    '''Test that resizing takes place when the resize_threshold is exceeded.'''
    ht = hash_table.Hash_Table(64, True)
    old_resize_threshold = ht.resize_threshold
    needed_to_resize = (old_resize_threshold - ht.filled) * 2 - 1
    _ = [ht.insert(item, dictionary[item]) 
            for i, item in enumerate(dictionary) if i < needed_to_resize]
    assert ht.resize_threshold == old_resize_threshold * ht.resize_factor
