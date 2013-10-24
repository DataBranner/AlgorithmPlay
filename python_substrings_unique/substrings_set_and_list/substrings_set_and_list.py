# substrings_set_and_list.py
# 20131007, works
# David Prager Branner

import random
import string

def find_substring(s, max_uniq = 2):
    '''Given a string, return one example of its longest substring containing no
more than two (or other specified quantity of) unique characters.'''
    ##################
    # Eliminate minimal examples
    ##################
    if len(s) <= max_uniq:
        return s
    #
    ##################
    # Preparation
    ##################
    # Keep track of longest substring found yet.
    length_longest = 0
    #
    # Keep track of running current substring
    # Start and end indices in s (faster than storing or incrementing strings):
    start_i_running, end_i_running, length_running = (0, 1, 1)
    # Set of unique chars in running substring.
    unique_running = set(s[0])
    # List of characters added to unique_running, each as a tuple with its
    # index in s (item, index), in the order they were added to unique_running.
    chars_found = [(s[0], 0)]
    # Cursor to move through chars_found so we know where we are in it.
    cursor = 0
    #
    ##################
    # Substring search
    ##################
    for i, item in enumerate(s):
        # Extend end of running substring to current character
        end_i_running = i + 1
        if item in unique_running:
            # If already in unique_running,
            # decide if item is different from the previous index.
            if i > 0 and s[i] != s[i-1]:
                # Append it, so that chars_found represents a sequence of
                # different chars, not just totally new ones.
                chars_found.append((item, i))
        else:
            # If not in unique, several steps:
            # 1) add to unique_running;
            unique_running.add(item)
            # 2) add to chars_found, move cursor forward one item;
            chars_found.append((item, i))
            # 3) check that unique range is of prescribed cardinality.
            while cursor + max_uniq < len(chars_found):
                # pop first item from unique...
                # Debugging output
#                print('    removing', s[start_i_running],
#                        'from unique_running')
                _ = unique_running.remove(s[start_i_running])
                cursor += 1
                start_i_running = chars_found[cursor][1]
                # ... but restore items found to have been popped wrongly.
                candidate_char = chars_found[cursor][0]
                if candidate_char not in unique_running:
                    unique_running.add(candidate_char)
        # Recalculate length of running substring and compare to longest.
        length_running = end_i_running - start_i_running
        if length_running > length_longest:
            start_i_longest, end_i_longest, length_longest = (
                    start_i_running, end_i_running, length_running)
        # Debugging output
#        print('''state: ''',
#                '''\n    longest: {}; current {}'''
#                '''\n    unique_running: {}'''.
#                format(s[start_i_longest:end_i_longest],
#                    s[start_i_running:end_i_running], unique_running))
    return s[start_i_longest:end_i_longest]

def test_random(length = 100, max_uniq = 2):
    '''Allows manual testing to see if function find_substring() returns
substrings that are longer than allowed.'''
    s = ''.join([random.choice(string.ascii_uppercase) for i in range(length)])
    result = find_substring(s, max_uniq)
    if len(set(result)) > max_uniq:
        print('len(set(result)):', len(set(result)), 'max_uniq:',
                max_uniq, 'result:', result)
    else:
        print(result)
