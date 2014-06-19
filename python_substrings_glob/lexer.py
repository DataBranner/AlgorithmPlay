#! /usr/bin/env python
# lexer.py
# David Prager Branner
# 20140619

from collections import deque

actions = {'?': ('dot'),
        '*': ('star')}

def lexer(p):
    """For each char or char-set in pattern, return a tuple naming its type.
    """
    # deque() is idempotent; no harm in this on recursion.
    p = deque(p)
    lexed = []
    lexed_set = []
    while p:
        c = p.popleft()
        tag = 'char'
        if c == '\\':
            # Process following character as escaped.
            lexed.append((tag, p.popleft()))
        elif c == '[':
            # Handle character sets.
            c_set = p.popleft()
                # Special test of first character in set: neg. charsets, ].
                tag = 'set'
                if not lexed_set: 
                    if c_set in {'^', '!'}:
                        # Discard character but change tag.
                        tag = 'negset'
                else:
                    # Close-] can only be added if it is first char in set,
                    # the same as any other non-neg. character in that position.
                    lexed_set.append(c_set)
                # Characters after first are added until close-] encountered.
                while p:
                    c_set = p.popleft()
                    if c_set == '\\':
                        pass
            lexed.append((tag, lexed_set))
        else:
            lexer.append((tag, c))
    return p. lexed
