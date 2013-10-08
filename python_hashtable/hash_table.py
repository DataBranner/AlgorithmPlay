# hash_table.py
# 20130915
# David Prager Branner

'''Models a simple hash table with list-based chaining and optional resizing.

Because built-in hashes may be positive or negative, I double the chances of
collision. I could avoid this by adding sys.maxsize before hashing, but that
would cost time converting to a long integer.

'''

import random

class Hash_Table(object):
    def __init__(self, size=16, resizeable=False):
        self.size = size
        self.array = [None for i in range(self.size)]
        self.resizeable = resizeable
        self.resize_threshold = int(self.size / 2)
        self.resize_factor = 2
        self.filled = 0

    def insert(self, key, value, the_hash=None):
        '''Inserts a tuple: key, value, hash; the hash is included in order not
        to repeat work on resizing.'''
        if not the_hash:
            the_hash = hash(key)
        index = the_hash % self.size
        # Check for collision.
        if self.array[index]:
            self.insert_collis(index, key, value, the_hash)
        else:
            self.array[index] = (key, value, the_hash)
            self.filled += 1
            if self.resizeable and self.filled > self.resize_threshold:
                self.resize()

    def retrieve(self, key):
        '''Retrieves the value associated with a desired unique key.'''
        the_hash = hash(key)
        index = the_hash % self.size
        if isinstance(self.array[index], list):
            return self.retrieve_collis(index, key)
        else:
            return self.array[index][1]

    def insert_collis(self, index, key, value, the_hash):
        '''Inserts a tuple: key, value, hash, given that there is already
        content in the slot in question.'''
        if not isinstance(self.array[index], list):
            # First see if the existing value is solitary.
            if self.array[index][1] == value:
                return
            # Then change to list.
            else:
                self.array[index] = [self.array[index]]
        # If key already in list, replace value there.
        for i, item in enumerate(self.array[index]):
            if item[0] == key:
                self.array[index][i] = (key, value, the_hash)
                break
        # Otherwise, append new tuple.
        else:
            self.array[index].append((key, value, the_hash))

    def retrieve_collis(self, index, key):
        '''Retrieves the value associated with a desired unique key, given that
        the slot in question contains a list.'''
        # There is already a list at the index, so search the list for key.
        for i, item in enumerate(self.array[index]):
            if item[0] == key:
                return item[1]
        return None

    def resize(self):
        '''Resizes array by resize_factor and sets new resize_threshold.'''
        old_array = self.array
        self.size *= self.resize_factor
        self.resize_threshold = int(self.size / 2)
        self.array = [None for i in range(self.size)]
        self.filled = 0
        # Turn off resizing while populating new array, since insert() would
        # otherwise call resize().
        self.resizeable = False
        # Handle all three possible types of content in old_array:
        for item in old_array:
            if not item:
                continue
            if not isinstance(item, list):
                index = item[2] % self.size
                self.insert(*item)
            else:
                for subitem in item:
                    index = subitem[2] % self.size
                    self.insert(*subitem)
        # Populating of new array is complete; turn resizing back on.
        self.resizeable = True

def create(size=16, resizeable=False):
    '''Instantiates object.'''
    hash_table = Hash_Table(size, resizeable)
    return hash_table
