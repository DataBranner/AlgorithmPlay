# anagrams.py
# David Prager Branner
# 20131205
""""""

import os, sys

def anagrams(filename = 'dict.txt', minlength = 4, maxlength = 6):
    # prepare `to_return`: list of lists to be returned
    to_return = []
    # get data from file
    with open(os.path.join('DATA', filename)) as f:
        data = f.read()
    # sort into sets, one set per given length of word; list `sets`
    #       (minlength <= length <= maxlength)
    # for each set in `sets`: 
        # begin while loop until set is empty
        # pop a word and sort its characters; we call this the "target"
        # create new list for the target
        # iterate through remaining words and:
            # sort each
            # if it matches target, add it to target's list and pop it from set
        # if target's list is > length 1, add to else abandon
    return to_return
    
