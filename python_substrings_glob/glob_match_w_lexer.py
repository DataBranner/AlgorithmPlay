#! /usr/bin/env python
# glob_match_w_lexer.py
# David Prager Branner
# 20140619

"""Perform simple glob (global wildcard expansion) match on input string."""

from collections import deque
import lexer as L

def main(p, s):
    """Use cursors, a queue, and memoization to match glob pattern to string."""
    # Populate initial variables.
    p_cursor = 0
    s_cursor = 0
    cursor_pair_queue = deque([(p_cursor, s_cursor)])
    cursor_pairs_seen = {}
    # Add all elements of string to dictionary of actions.
    actions = {'char': count_character,
            'question_mark': question_mark,
            'star': star,
            'set': check_set,
            'negset': check_negset}
    # Prune any redundant * in pattern.
    while '**' in p:
        p = p.replace('**', '*')
    # Process pattern with lexer.
    p = L.lexer(p)
    print('lexed p:', p)
    # Start traversing string and adding cursor-pairs to queue.
    while cursor_pair_queue:
        print('cursor_pair_queue:', cursor_pair_queue)
        p_cursor, s_cursor = cursor_pair_queue.popleft()
        # Eliminate cursor-pairs already examined or having invalid s-cursor.
        if (p_cursor, s_cursor) in cursor_pairs_seen or s_cursor == len(s):
            continue
        else:
            cursor_pairs_seen[(p_cursor, s_cursor)] = True
        # Get next character of pattern
        if p_cursor < len(p):
            next_char = p[p_cursor][0]
        else:
            continue
        # Compare character-pairs.
        try:
            new_pairs = actions[next_char](p, s, p_cursor, s_cursor)
        except KeyError:
            print('KeyError: {}'.format(next_char))
            return False
        print('s_cursor {} len(s) - 1 {}  p_cursor {} len(p) - 1 {}'.
                format(s_cursor, len(s) - 1, p_cursor, len(p) - 1))
        if new_pairs:
            if s_cursor == len(s) - 1 and p_cursor == len(p) - 1:
                return True
            cursor_pair_queue.extend(new_pairs)
    # If we are here, queue is empty but either p or s is not yet used up.
    return False

def count_character(p, s, p_cursor, s_cursor):
    """Advance both cursors if exact match."""
    if p[p_cursor][1] == s[s_cursor]:
        return [(p_cursor + 1, s_cursor + 1)]
    else:
        return None

def question_mark(p, s, p_cursor, s_cursor):
    """Advance both cursors on any character."""
    return [(p_cursor + 1, s_cursor + 1)]

def star(p, s, p_cursor, s_cursor):
    """Return three different cursor-pairs."""
    return [(p_cursor + 1, s_cursor),     # * matches 0 characters
            (p_cursor + 1, s_cursor + 1), # * matches 1 character
            (p_cursor, s_cursor + 1)      # * matches > 1 characters
            ]

def check_set(p, s, p_cursor, s_cursor):
    """Advance both cursors if item from s is in set from p."""
    print('in check_negset; s[s_cursor] {} p[p_cursor][1] {}'.
            format(s[s_cursor], p[p_cursor][1]))
    if s[s_cursor] in p[p_cursor][1]:
        return [(p_cursor + 1, s_cursor + 1)]
    else:
        return None

def check_negset(p, s, p_cursor, s_cursor):
    """Advance both cursors if item from s is *not* in set from p."""
    print('in check_negset; s[s_cursor] {} p[p_cursor][1] {}'.
            format(s[s_cursor], p[p_cursor][1]))
    if s[s_cursor] in p[p_cursor][1]:
        return None
    else:
        return [(p_cursor + 1, s_cursor + 1)]
if __name__ == '__main__':
    main()
