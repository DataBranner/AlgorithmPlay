#! /usr/bin/env python
# glob_match_with_print.py
# David Prager Branner
# 20140604, works

"""Perform simple glob (global wildcard expansion) match on input string."""

from collections import deque

def main(p, s):
    """Use cursors, a queue, and memoization to match glob pattern to string."""
    print('This program describes the decisions that are being made at each '''
            '''step. For silent running, use `glob_match.py`.\n''')
    # Populate initial variables.
    p_cursor = 0
    s_cursor = 0
    cursor_pair_queue = deque([(p_cursor, s_cursor)])
    cursor_pairs_seen = {}
    to_return = None
    pop_counter = 0
    # Prune any redundant * in pattern.
    while '**' in p:
        p = p.replace('**', '*')
        print('    Pruning redundant * in pattern.')
    print('    Using pattern {}.'.format(p))
    # Add all elements of string to dictionary of actions.
    actions = {c: count_character for c in set(s)}
    actions['?'] = question_mark
    actions['*'] = star
    # Start traversing string and adding cursor-pairs to queue.
    while cursor_pair_queue:
        p_cursor, s_cursor = cursor_pair_queue.popleft()
        pop_counter += 1
        # Eliminate cursor-pairs already examined or having invalid s-cursor.
        if (p_cursor, s_cursor) in cursor_pairs_seen or s_cursor == len(s):
            if (p_cursor, s_cursor) in cursor_pairs_seen:
                print('''    Cursor pair {}:{} has already been examined; '''
                '''discarding.'''.format(p_cursor, s_cursor))
            else:
                print('''    String cursor has exceeded length of string; '''
                '''discarding cursor pair {}:{}.'''.format(p_cursor, s_cursor))
            continue
        else:
            cursor_pairs_seen[(p_cursor, s_cursor)] = True
        # Get next character of pattern
        if p_cursor < len(p):
            next_char = p[p_cursor]
        else:
            print('    Discard {} because p_cursor >= len(p).'.
                    format((p_cursor, s_cursor)))
            continue
        print('\n{}:{} (cursors p={} : s={})'.
                format(p[p_cursor], s[s_cursor], p_cursor, s_cursor))
        # Compare character-pairs.
        try:
            print('    function called: {}'.format(actions[next_char].__name__))
            new_pairs = actions[next_char](p, s, p_cursor, s_cursor)
        except KeyError:
            print('''    Match has failed because character {} in pattern '''
                    '''is not in string'''.format(next_char))
            to_return = False
            break
        print('    function {} returns: {}'.
                format(actions[next_char].__name__, new_pairs))
        if new_pairs:
            if s_cursor == len(s) - 1 and p_cursor == len(p) - 1:
                print('''    Match has succeeded because cursors are both '''
                        '''at the last indices of their strings: '''
                        '''\np: {}, s: {}.'''.
                        format(p_cursor, s_cursor)
                to_return = True
                break
            cursor_pair_queue.extend(new_pairs)
        print('    queue is now {}'.format(cursor_pair_queue))
    # If we are here, either p or s is not yet used up.
    print('''    Final state of queue: {}.'''.format(cursor_pair_queue))
    print('''    Total number of cursor-pairs popped from queue: {}.'''.
            format(pop_counter))
    if to_return == None:
        print('''\nMatch has failed.''')
        if s_cursor < len(s) - 1:
            print('''    Cursor-pair queue is empty but '''
                    '''string is not yet used up.''')
        if p_cursor < len(p) - 1:
            print('''    Cursor-pair queue is empty but '''
                    '''pattern is not yet used up.''')
    print('''\nFinal state:'''
            '''\n    s_cursor: {}, last index of s: {}'''
            '''\n    p_cursor: {}, last index of p: {}'''.
            format(s_cursor, len(s) - 1, p_cursor, len(p) - 1))
    return to_return

def count_character(p, s, p_cursor, s_cursor):
    """Advance both cursors if exact match."""
    if p[p_cursor] == s[s_cursor]:
        return [(p_cursor + 1, s_cursor + 1)]

def question_mark(p, s, p_cursor, s_cursor):
    """Advance both cursors on any character."""
    return [(p_cursor + 1, s_cursor + 1)]

def star(p, s, p_cursor, s_cursor):
    """Return three different cursor-pairs."""
    return [(p_cursor + 1, s_cursor),     # * matches 0 characters
            (p_cursor + 1, s_cursor + 1), # * matches 1 character
            (p_cursor, s_cursor + 1)      # * matches > 1 characters
            ]

if __name__ == '__main__':
    main()
