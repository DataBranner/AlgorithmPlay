# anagrams.py
# David Prager Branner
# 20131205
"""Given a dictionary, output the top 20 most "anagrammable" 4-, 5-, and
6-letter words."""

import os, sys

def anagrams(path = 'DATA', filename = 'dict.txt', 
        minlength = 4, maxlength = 6):
    # prepare `to_return`: list of lists to be returned; and other variables
    to_return = []
    number_sets = maxlength - minlength + 1
    sets_by_length = [set() for i in range(number_sets)]
    print(sets_by_length)
    # get data from file
    with open(os.path.join(path, filename)) as f:
        data = f.read()
    data = data.split()
    data = data[:2000]
    # sort into sets, one set per given length of word; list `sets`
    #       (minlength <= length <= maxlength)
    for item in data:
        index = len(item)
        if minlength <= index <= maxlength:
            # sort into correct set
            print(item, index)
#            print('target set:', sets_by_length[index - minlength])
            sets_by_length[index - minlength].add(item)
    print(sets_by_length) # debug
    # for each set in `sets`: 
    for one_set in sets_by_length:
        # begin while loop until set is empty
        while one_set:
            word = one_set.pop()
        # pop a word, delete punctuation, sort its chars; we call this "target"
        # create new list for the target
        # iterate through remaining words and:
            # sort each
            # if it matches target, add it to target's list and pop it from set
        # if target's list is > length 1, add to else abandon
    print(sets_by_length) # debug
    return to_return
    
