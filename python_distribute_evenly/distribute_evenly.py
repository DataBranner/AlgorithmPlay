#! /usr/bin/env python
# distribute_evenly.py
# David Prager Branner
# 20140605, not yet working

"""Make sure each collection (numbered by integers from 1)
has a copy of each other collection."""

import random

def main(number):
    # Each collection is a set containing copy-numbers.
    # We are counting from 1 so will always leave index 0 empty and will use
    #     a separate variable, incremented by 1, in loops and comprehensions.
    collections = [None]
    # Assign a copy's number to any collection possessing it.
    # "Copy_in_collection" indexes where a given copy can be found.
    copy_in_collection = {i + 1: [] for i in range(number)}
    for collection in range(number):
        collection_number = collection + 1
        line = raw_input()
        line = [int(i) for i in line.split()]
        collections.append(set(line))
        for i in line:
            copy_in_collection[i].append(collection_number)
    print('collections: {}\ncopy_in_collection: {}'.
            format(collections, copy_in_collection))
    #
    # For each collection, find missing copies and supply them from where 
    # they're found.
    to_move = {i: [] for i in xrange(1, number + 1)}
    print(to_move)
    full_set = {i + 1 for i in range(number)}
    print(full_set)
    for i, collection in enumerate(collections[1:]):
        i += 1
        print('\ni:', i)
        difference = full_set - collection
        print('difference:', difference)
        if difference:
            for j in difference:
                print('j:', j)
                source = random.sample(copy_in_collection[j], 1)
                to_move[source].append(i)
    #
    # Print output.
    return to_move
