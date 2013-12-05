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
#    print(sets_by_length)
    # get data from file
    with open(os.path.join(path, filename)) as f:
        data = f.read()
    data = data.split()
#    data = data[:20000]
    # sort into sets, one set per given length of word; list `sets`
    #       (minlength <= length <= maxlength)
    for item in data:
        index = len(item)
        if minlength <= index <= maxlength:
            # sort into correct set
#            print(item, index)
#            print('target set:', sets_by_length[index - minlength])
            sets_by_length[index - minlength].add(item)
#    print(sets_by_length) # debug
    # for each set in `sets`: 
    for one_set in sets_by_length:
        print('Now treating words of length', len(one_set))
        # begin while loop until set is empty
        while one_set:
            # pop a word, strip punctuation, sort its chars; 
            # we call this "target"
            # create new list for the target
            target = one_set.pop()
            targets_list = [target]
            target_cleaned = clean_and_alphabetize(target)
#            print('cleaned target:', target_cleaned)
            # iterate through remaining words
            list_of_one_set = list(one_set)
            for word in list_of_one_set:
                # strip off punctuation and sort each
                word_cleaned = clean_and_alphabetize(word)
                # if it matches target, 
                #     add it to target's list and remove it from set
                if word_cleaned == target_cleaned:
                    targets_list.append(word)
                    one_set.remove(word)
#                    print('word', word, 'removed from set')
#                    print('target', target, 'added')
                    print('.', end='')
            # if target's list is > length 1, add to `to_return`, else abandon
            length_of_list = len(targets_list)
            if length_of_list > 1:
                to_return.append((length_of_list, targets_list))
#                print('length', length_of_list, 'targets_list', targets_list, 
#                        'added')
#    print(sets_by_length) # debug
    to_return.sort(reverse = True)
    return to_return[0:20]

def clean_and_alphabetize(word):
    cleaned = ''.join(word.lower().split('-'))
    return ''.join(sorted(list(cleaned)))
