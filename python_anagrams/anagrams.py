#! /usr/local/bin/python3
# anagrams.py
# David Prager Branner
# 20131205, works.
"""Given a dictionary, output the top 20 most "anagrammable" 4-, 5-, and
6-letter words."""

import os

def main(path = 'DATA', filename = 'dict.txt',
        minlength = 4, maxlength = 6, top_quant_to_print = 20):
    # Prepare variables.
    number_sets = maxlength - minlength + 1
    alphagrams_by_length = [{} for i in range(number_sets)]
    # Get data from file
    with open(os.path.join(path, filename)) as f:
        data = f.read()
    data = data.split()
    # Sort into sets, one set per given length of word; list `sets`
    #       (minlength <= length <= maxlength)
    #
    # Remember that we have (20131205) two words containing hyphens, so we
    # always work with a cleaned alphagram of a given word (see function
    # make_alphagram(), below). We use these forms as the keys in the
    # several dictionaries contained in alphagrams_by_length, but we need to be
    # able to return the original words, too, so we can't discard them.
    for item in data:
        item_cleaned = make_alphagram(item)
        index = len(item_cleaned)
        if minlength <= index <= maxlength:
            # Sort into correct dictionary.
            if item_cleaned in alphagrams_by_length[index-minlength]:
                alphagrams_by_length[index-minlength][item_cleaned].extend(
                        [item])
            else:
                alphagrams_by_length[index-minlength][item_cleaned] = [item]
    for length, one_dict in enumerate(alphagrams_by_length):
        print('\nTop {} most anagrammable {}-letter words:\n'.
                format(top_quant_to_print, length + minlength))
        # Count the number of alphagrams in each item in dict.
        hits = {}
        for item in one_dict:
            item_length = len(one_dict[item])
            if item_length in hits:
                hits[item_length].extend([item])
            else:
                hits[item_length] = [item]
        # Return the anagraphs corresponding to the top alphagrams in the dict.
        counter = 0
        for the_key in sorted(hits, reverse = True):
            alphagrams = hits[the_key]
            for item in alphagrams:
                if counter <= top_quant_to_print:
                    counter += 1
                    print(one_dict[item])

    return

def make_alphagram(word):
    # In future, we may like to check file for any non-ASCII characters and add
    # to a string of to-strip characters.
    cleaned = ''.join(word.lower().split('-'))
    return ''.join(sorted(list(cleaned)))

if __name__ == '__main__':
    main()
