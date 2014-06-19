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

def test_07():
    """Test single-character wildcard."""
    p = 'a?bc'
    assert L.lexer(p) == [('char', 'a'), ('question_mark', '?'), ('char', 'b'),
            ('char', 'c')]

def test_08():
    """Test Kleene star wildcard."""
    p = 'a*bc'
    assert L.lexer(p) == [('char', 'a'), ('star', '*'), ('char', 'b'), ('char',
            'c')]

def test_09():
    """Test asterisk in character set, not as Kleene star; and 1-char set."""
    p = 'a[*]bc'
    assert L.lexer(p) == [('char', 'a'), ('char', '*'), ('char', 'b'),
            ('char', 'c')]

def test_10():
    """Test escaped asterisk, not as Kleene star."""
    p = 'a\*bc'
    assert L.lexer(p) == [('char', 'a'), ('char', '*'), ('char', 'b'), ('char',
            'c')]

def test_11():
    """Close-] within character set, and 1-char set => str."""
    p = 'a[]]bc'
    assert L.lexer(p) == [('char', 'a'), ('char', ']'), ('char', 'b'),
            ('char', 'c')]

def test_12():
    """Close-] and open-[ within character set."""
    p = 'a[][]bc'
    assert L.lexer(p) == [('char', 'a'), ('set', {'[', ']'}), ('char', 'b'),
            ('char', 'c')]
