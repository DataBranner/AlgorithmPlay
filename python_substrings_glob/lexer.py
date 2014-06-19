#! /usr/bin/env python
# lexer.py
# David Prager Branner
# 20140618

def lexer(p):
    """For each char or char-set in pattern, return a tuple naming its type."""
    lexed = []
    for c, c2 in zip(p, p[1:]):
        if c == '\\':
            # Process following character as escaped.
            lexed.append(('char', c2))
        elif c == '[':
            # Handle character sets.
            pass
        else:
            lexer.append(('char', c))
    return lexed
