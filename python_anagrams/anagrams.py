# anagrams.py
# David Prager Branner
# 20131205
""""""

import os, sys

def anagrams(path = 'DATA', filename = 'dict.txt', 
        minlength = 4, maxlength = 6):
    # prepare `to_return`: list of lists to be returned; and other variables
    to_return = []
    number_sets = maxlength - minlength + 1
    sorted_sets = [set() for i in range(number_sets)]
    print(sorted_sets)
    # get data from file
    with open(os.path.join(path, filename)) as f:
        data = f.read()
    data = data.split()
    data = data[:20]
    # sort into sets, one set per given length of word; list `sets`
    #       (minlength <= length <= maxlength)
    for item in data:
        index = len(item)
        if minlength <= index <= maxlength:
            # sort into correct set
            print(item, index)
            print('target set:', sorted_sets[index - minlength])
            sorted_sets[index - minlength].add(item)
#            print('added', item, 'to', sorted_sets[index - minlength])
            print(sorted_sets)
    # for each set in `sets`: 
        # begin while loop until set is empty
        # pop a word and sort its characters; we call this the "target"
        # create new list for the target
        # iterate through remaining words and:
            # sort each
            # if it matches target, add it to target's list and pop it from set
        # if target's list is > length 1, add to else abandon
    return to_return
    
