# test_lexer.py

import lexer as L

def test_01():
    """Test simple string."""
    p = 'abcde'
    assert L.lexer(p) == [('char', 'a'), ('char', 'b'), ('char', 'c'), ('char',
            'd'), ('char', 'e')]

def test_02():
    """Test simple character set."""
    p = 'ab[cd]e'
    assert L.lexer(p) == [('char', 'a'), ('char', 'b'), ('set', {'c', 'd'}),
            ('char', 'e')]

def test_03():
    """Test negative character set."""
    p = 'ab[^cd]e'
    assert L.lexer(p) == [('char', 'a'), ('char', 'b'), ('negset', {'c', 'd'}),
            ('char', 'e')]

def test_04():
    """Test negative character set."""
    p = 'ab[!cd]e'
    assert L.lexer(p) == [('char', 'a'), ('char', 'b'), ('negset', {'c', 'd'}),
            ('char', 'e')]

def test_05():
    """Test wildcard within character set."""
    p = 'a\?bcd'
    assert L.lexer(p) == [('char', 'a'), ('char', '?'), ('char', 'b'), 
            ('char', 'c'), ('char', 'd')]

def test_06():
    """Test negative symbol as character within character set."""
    p = 'abc^d'
    assert L.lexer(p) == [('char', 'a'), ('char', 'b'), ('char', 'c'), ('char',
            '^'), ('char', 'd')]
