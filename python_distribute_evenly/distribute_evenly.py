#! /usr/bin/env python
# distribute_evenly.py
# David Prager Branner
# 20140606, working

"""Make sure each collection (numbered by integers from 1)
has a copy of each other collection.

Input is a multi-line string of space-delimited series of integers, e.g.
    1 3 4\n
    1 2 3\n
    1 3\n
    1 4 2
The first list represents the first collection, the second list the second collection, etc. The integers in a given collection represent the collections that have a copy of that collection-number's data. So the first line above reads "Collection 1 (because it is line 1) has copies of collections 1, 3, and 4."

Output is a series of instructions enabling copies to be moved between collections until all collections have a copy of all the collections. It is formatted a list of space delimited strings, each containing three integers. E.g.
    ['2 4 1', '4 1 2', '2 2 3', '4 1 3', '3 2 4']
Each string is an instruction. '2 4 1' means "Take the copy of collection 2 located at collection 4 and send it to collection 1."
"""

# Debug-print statements have been left in, but are commented out.

import random

def main(string_of_lines):
    # Each collection is a set containing copy-numbers.
    # Break string into list of sets.
    set_of_int_chars = [set(line.split()) 
            for line in string_of_lines.split('\n')]
#    print('set_of_int_chars:', set_of_int_chars)
    # (We are counting from 1 so will always leave index 0 empty and will use
    #     a separate variable, incremented by 1, in loops and comprehensions.)
    collections = [None] + [
            set([int(i) for i in subset]) for subset in set_of_int_chars ]
#    print('collections:', collections)
    #
    # Find largest collection number.
    number = max(max(item) for item in collections[1:])
#    print('number:', number)
    # Assign a copy's number to any collection possessing it.
    # "Copy_in_collection" indexes where a given copy can be found.
    copy_in_collection = {i + 1: set() for i in range(number)}
    for collection_number, collection in enumerate(collections[1:]):
        collection_number = collection_number + 1
        for i in collection:
#            print('\ni:', i, 'collection_number:', collection_number)
            copy_in_collection[i].add(collection_number)
    print('collections: {}\ncopy_in_collection: {}'.
            format(collections, copy_in_collection))
    #
    # For each collection, find missing copies and supply them from where 
    # they are found.
    to_move = []
#    print('to_move:', to_move)
    full_set = {i + 1 for i in range(number)}
#    print('full_set:', full_set)
    for collection_number, collection in enumerate(collections[1:]):
        collection_number += 1
#        print('\ncollection_number:', collection_number)
        those_missing = full_set - collection
#        print('difference:', those_missing)
        if those_missing:
            for one_missing in those_missing:
#                print('one_missing:', one_missing)
                if copy_in_collection[one_missing] == set():
                    # If no copies of a collection exist, nothing can be done.
                    continue
                # On what basis to choose where to take copy from?
                # Using `random.sample(copy_in_collection[one_missing], 1)[0]` 
                # makes output less regular, hence harder to test; prefer 
                # `next(iter())` instead.
                source = next(iter(copy_in_collection[one_missing]))
#                print('source:', source)
                to_move.append(
                        str(one_missing) + ' ' + 
                        str(source) + ' ' + 
                        str(collection_number))
    return to_move
