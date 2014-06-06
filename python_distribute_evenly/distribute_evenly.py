#! /usr/bin/env python
# distribute_evenly.py
# David Prager Branner
# 20140606, working

"""Make sure each library has the catalog of each other library.

Input is a multi-line string of space-delimited series of integers, e.g.

    1 3 4\n
    1 2 3\n
    1 4\n
    1 3 2

The first list represents the first library, the second list the second library, etc. The integers in a given library represent the libraries that have a copy of that library's catalog. So the first line above reads "library 1 (because it is line 1) has catalogs of libraries 1, 3, and 4."

Output is a series of instructions enabling copies to be moved between libraries until all libraries have a catalog of all the libraries. It is formatted a list of space delimited strings, each containing three integers. E.g.

    ['2 2 1', '4 1 2', '2 2 3', '3 1 3', '4 1 4']

Each string is an instruction. '2 2 1' means "Take the catalog of library 2 located at library 2 and send it to library 1."
"""

# Debug-print statements have been left in, but are commented out.

import random

def main(string_of_lines):
    # Each library is a set containing catalog-numbers.
    # Break string into list of sets.
    set_of_int_chars = [set(line.split()) 
            for line in string_of_lines.split('\n')]
#    print('set_of_int_chars:', set_of_int_chars)
    #
    # (We are counting from 1 so will always leave index 0 empty and will use
    #     a separate variable, incremented by 1, in loops and comprehensions.)
    libraries = [None] + [
            set([int(i) for i in subset]) for subset in set_of_int_chars ]
#    print('libraries:', libraries)
    #
    # Find largest library number.
    number = max(max(item) for item in libraries[1:])
#    print('number:', number)
    #
    # Assign a catalog's number to any library possessing it.
    # "catalog_in_library" indexes where a given catalog can be found.
    catalog_in_library = {i + 1: set() for i in range(number)}
    for library_number, library in enumerate(libraries[1:]):
        library_number = library_number + 1
        for i in library:
#            print('\ni:', i, 'library_number:', library_number)
            catalog_in_library[i].add(library_number)
    print('libraries: {}\ncatalog_in_library: {}'.
            format(libraries, catalog_in_library))
    #
    # For each library, find missing catalogs and supply them from wherever
    # they are found.
    to_move = []
#    print('to_move:', to_move)
    full_set = {i + 1 for i in range(number)}
#    print('full_set:', full_set)
    for library_number, library in enumerate(libraries[1:]):
        library_number += 1
#        print('\nlibrary_number:', library_number)
        those_missing = full_set - library
#        print('difference:', those_missing)
        if those_missing:
            for one_missing in those_missing:
#                print('one_missing:', one_missing)
                if catalog_in_library[one_missing] == set():
                    # If no copies of a library exist, nothing can be done.
                    continue
                # On what basis to choose where to take catalog from?
                # Using `random.sample(catalog_in_library[one_missing], 1)[0]` 
                # makes output less regular, hence harder to test; prefer 
                # `next(iter())` instead.
                source = next(iter(catalog_in_library[one_missing]))
#                print('source:', source)
                to_move.append(
                        str(one_missing) + ' ' + 
                        str(source) + ' ' + 
                        str(library_number))
    return to_move
