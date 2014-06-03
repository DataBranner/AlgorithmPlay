# test_glob_match.py
# David Prager Branner
# 20140602

"""Test glob.py."""

import re
import sys
sys.path.append('..')
import glob_match

def glob_to_regex(s):
    s = s.replace(r'*', r'.*')
    s = s.replace(r'?', r'.')
    return s


def test_glob_01():
    s = 'abaaaabbbbbb'
    pattern = 'a?*b'
