# substrings_list_only.py
# 20131007, works.
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
    # List of characters encountered and another of their indices in s.
    chars_found = [s[0]]
    chars_found_i = [0]
    # Cursor to move through chars_found so we know where we are in it.
    cursor = 0
    #
    ##################
    # Substring search
    ##################
    for i, item in enumerate(s):
        # Extend end of running substring to current character
        end_i_running = i + 1
        if item in chars_found[start_i_running:end_i_running]:
            # If already in chars_found,
            # decide if item is different from the previous index.
            if i > 0 and s[i] != s[i-1]:
                # Append it, so that chars_found represents a sequence of
                # different chars, not just totally new ones.
                chars_found.append(item)
                chars_found_i.append(i)
        else:
            # If not in unique range, two steps:
            # 1) add to chars_found, move cursor forward one item;
            chars_found.append(item)
            chars_found_i.append(i)
            # 2) check that unique range is of prescribed cardinality.
            while cursor + max_uniq < len(chars_found):
                # delete superfluous item(s), starting at smallest index.
                # Debugging output
#                print('    moving up cursor from', cursor, end=' ')
                cursor += 1
#                print('to', cursor)
                start_i_running = chars_found_i[cursor]
        # Recalculate length of running substring and compare to longest.
        length_running = end_i_running - start_i_running
        if length_running > length_longest:
            start_i_longest, end_i_longest, length_longest = (
                    start_i_running, end_i_running, length_running)
        # Debugging output
#        print('''state: ''',
#                '''\n    longest: {}; current {}'''
#                '''\n    chars_found: {}'''.
#                format(s[start_i_longest:end_i_longest],
#                    s[start_i_running:end_i_running], chars_found))
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
