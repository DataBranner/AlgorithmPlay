# test_substrings_list_only.py
# David Prager Branner
# 20131005, works.

import pytest
import random
import string
import os
import sys
sys.path.append(os.path.join('../substrings_list_only'))
import substrings_list_only

# The following nine tests use strings that caused difficulty during coding.

def test_two_unique_01():
    assert substrings_list_only.find_substring('banana', 2) == 'anana'

def test_two_unique_02():
    assert substrings_list_only.find_substring('bookkeeper') in ['kkee', 'ookk', 'eepe']

def test_two_unique_03():
    assert substrings_list_only.find_substring('aaaaa', 2) == 'aaaaa'

def test_two_unique_04():
    assert substrings_list_only.find_substring('', 2) == ''

def test_two_unique_05():
    assert substrings_list_only.find_substring('a', 2) == 'a'

def test_two_unique_06():
    assert substrings_list_only.find_substring('abcabcabcabcdd', 2) == 'cdd'

def test_two_unique_07():
    s = 'anannannnannnnannnnnannnnnnannnnnnn'
    assert substrings_list_only.find_substring(s, 2) == s

def test_two_unique_08():
    assert substrings_list_only.find_substring('babccc', 2) == 'bccc'

def text_two_unique_09():
    assert substrings_list_only.find_substring('baaabccc', 2) == 'baaab'

# The following six tests use random strings to see whether substrings longer
# than permitted are produced.

def test_random_unique_01():
    max_uniq = 10
    s = ''.join([random.choice(string.ascii_uppercase) for i in range(10000)])
    result = substrings_list_only.find_substring(s, max_uniq)
    assert len(set(result)) <= max_uniq

def test_random_unique_02():
    max_uniq = 8
    s = ''.join([random.choice(string.ascii_uppercase) for i in range(10000)])
    result = substrings_list_only.find_substring(s, max_uniq)
    assert len(set(result)) <= max_uniq

def test_random_unique_03():
    max_uniq = 5
    s = ''.join([random.choice(string.ascii_uppercase) for i in range(10000)])
    result = substrings_list_only.find_substring(s, max_uniq)
    assert len(set(result)) <= max_uniq

def test_random_unique_05():
    max_uniq = 3
    s = ''.join([random.choice(string.ascii_uppercase) for i in range(10000)])
    result = substrings_list_only.find_substring(s, max_uniq)
    assert len(set(result)) <= max_uniq

def test_random_unique_06():
    max_uniq = 2
    s = ''.join([random.choice(string.ascii_uppercase) for i in range(1000)])
    result = substrings_list_only.find_substring(s, max_uniq)
    assert len(set(result)) <= max_uniq
