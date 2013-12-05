# anagrams.py
# David Prager Branner
# 20131205
"""Given a dictionary, output the top 20 most "anagrammable" 4-, 5-, and
6-letter words."""

import os

def anagrams(path = 'DATA', filename = 'dict.txt', 
        minlength = 4, maxlength = 6, how_many_top_to_print = 20):
    # Prepare variables.
    number_sets = maxlength - minlength + 1
    anagrams_by_length = [[] for i in range(number_sets)]
    sets_by_length = [set() for i in range(number_sets)]
    # Get data from file
    with open(os.path.join(path, filename)) as f:
        data = f.read()
    data = data.split()
#    data = data[:50000]
    # Sort into sets, one set per given length of word; list `sets`
    #       (minlength <= length <= maxlength)
    #
    # Remember that we have (20131205) two words containing hyphens, so we
    # always work with a cleaned version of a given word (see
    # function clean_and_alphabetize(), below) when length or comparisons are
    # done.
    for item in data:
        index = len(clean_and_alphabetize(item))
        if minlength <= index <= maxlength:
            # Sort into correct set
            sets_by_length[index - minlength].add(item)
    for length, one_set in enumerate(sets_by_length):
        print('\nTop 20 most anagrammable {}-letter words:\n'.
                format(length + minlength))
        # Begin while loop until set is empty
        while one_set:
            # Pop a word ("target"), clean it and create new list for it.
            target = one_set.pop()
            target_cleaned = clean_and_alphabetize(target)
            targets_list = [target]
            # Iterate through remaining words in set
            list_of_one_set = list(one_set)
            for word in list_of_one_set:
                word_cleaned = clean_and_alphabetize(word)
                # If it matches target,
                #     add it to target's list and remove it from set
                if word_cleaned == target_cleaned:
                    targets_list.append(word)
                    one_set.remove(word)
            # If target's list is > length 1, add to `to_return`, else abandon
            length_of_list = len(targets_list)
            if length_of_list > 1:
                anagrams_by_length[length].append(
                        (length_of_list, targets_list))
        for i in range(how_many_top_to_print):
            to_print = sorted(anagrams_by_length[length], reverse = True)[:20]
            print(to_print[i][1], '\n')

def clean_and_alphabetize(word):
    cleaned = ''.join(word.lower().split('-'))
    return ''.join(sorted(list(cleaned)))
