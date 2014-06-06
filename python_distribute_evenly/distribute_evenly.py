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
        line = input()
        line = [int(i) for i in line.split()]
        collections.append(set(line))
        for i in line:
            copy_in_collection[i].append(collection_number)
    print('collections: {}\ncopy_in_collection: {}'.
            format(collections, copy_in_collection))
    #
    # For each collection, find missing copies and supply them from where 
    # they're found.
    to_move = []
    print('to_move:', to_move)
    full_set = {i + 1 for i in range(number)}
    print('full_set:', full_set)
    for collection_number, collection in enumerate(collections[1:]):
        collection_number += 1
        print('\ncollection_number:', collection_number)
        all_missing = full_set - collection
        print('difference:', all_missing)
        if all_missing:
            for one_missing in all_missing:
                print('one_missing:', one_missing)
                source = random.sample(copy_in_collection[one_missing], 1)[0]
                print('source:', source)
                to_move.append(
                        str(one_missing) + ' ' + 
                        str(source) + ' ' + 
                        str(collection_number)
                        )
    #
    # Print output.
    to_move.append('done')
    return to_move
