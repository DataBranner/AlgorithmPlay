# test_glob_match.py
# David Prager Branner
# 20140603

"""Test glob.py."""

import re
import sys
sys.path.append('..')
import glob_match_w_lexer as G

def glob_to_regex(s):
    s = s.replace(r'*', r'.*')
    s = s.replace(r'?', r'.')
    s = '^' + s + '$'
    return s

def test_glob_01():
    s = 'abaaaabbbbbb'
    p = 'a?*b'
    assert G.main(p, s) == bool(re.search(glob_to_regex(p), s))

def test_glob_02():
    s = 'aaababbabbba'
    p = '*?*'
    assert G.main(p, s) == bool(re.search(glob_to_regex(p), s))

def test_glob_03():
    s = 'aaababbabbba'
    p = '*?*a'
    assert G.main(p, s) == bool(re.search(glob_to_regex(p), s))

def test_glob_04():
    s = 'aaababbabbba'
    p = '*?*b'
    assert G.main(p, s) == bool(re.search(glob_to_regex(p), s))

def test_glob_05():
    s = 'aaababbabbba'
    p = '*?*n'
    assert G.main(p, s) == bool(re.search(glob_to_regex(p), s))

def test_glob_06():
    s = 'aaababbabbba'
    p = '*'
    assert G.main(p, s) == bool(re.search(glob_to_regex(p), s))

def test_glob_07():
    s = 'aaababbabbba'
    p = '*b'
    assert G.main(p, s) == bool(re.search(glob_to_regex(p), s))

def test_glob_08():
    s = 'aaababbabbba'
    p = '*b*a'
    assert G.main(p, s) == bool(re.search(glob_to_regex(p), s))

def test_glob_09():
    s = 'aaababbabbba'
    p = '*ba'
    assert G.main(p, s) == bool(re.search(glob_to_regex(p), s))

def test_glob_10():
    s = 'aaababbabbba'
    p = '*baa'
    assert G.main(p, s) == bool(re.search(glob_to_regex(p), s))

def test_glob_11():
    s = 'aaababbabbba'
    p = 'a*b??b*a*ba'
    assert G.main(p, s) == bool(re.search(glob_to_regex(p), s))

def test_glob_12():
    s = 'aaababbabbba'
    p = 'a*b??bb*a*ba'
    assert G.main(p, s) == bool(re.search(glob_to_regex(p), s))

def test_glob_13():
    s = 'aaababbabbba'
    p = 'a*b?*'
    assert G.main(p, s) == bool(re.search(glob_to_regex(p), s))

def test_glob_14():
    s = 'aaababbabbba'
    p = 'a*b?*a*ba'
    assert G.main(p, s) == bool(re.search(glob_to_regex(p), s))

def test_glob_15():
    s = 'aaababbabbba'
    p = 'a*b?*aba'
    assert G.main(p, s) == bool(re.search(glob_to_regex(p), s))

def test_glob_16():
    s = 'aaababbabbba'
    p = 'a*b?b*a*ba'
    assert G.main(p, s) == bool(re.search(glob_to_regex(p), s))

def test_glob_17():
    s = 'aaababbabbba'
    p = 'aaa?a'
    assert G.main(p, s) == bool(re.search(glob_to_regex(p), s))

def test_glob_18():
    s = 'aaababbabbba'
    p = 'b*?*'
    assert G.main(p, s) == bool(re.search(glob_to_regex(p), s))

