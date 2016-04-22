import abacus

def single_chars_only(lst):
    """Confirm that no list-element has other than one char"""
    return all(len(i) == 1 for i in lst)

def integers_only(lst):
    """Confirm that no list-element contains other than integers as chars"""
    try:
        _ = [int(i) for i in lst]
    except:
        return False
    return True

def test_01():
    """Test one digit without carry"""
    first = ['4']
    second = ['5']
    expected = ['9']
    observed = abacus.abacus(first, second)
    assert single_chars_only(observed)
    assert integers_only(observed)
    assert observed == expected

def test_02():
    """Test one digit with carry"""
    first = ['4']
    second = ['7']
    expected = ['1', '1']
    observed = abacus.abacus(first, second)
    assert single_chars_only(observed)
    assert integers_only(observed)
    assert observed == expected

def test_03():
    """Test two digits without carry"""
    first = ['4', '2']
    second = ['1', '7']
    expected = ['5', '9']
    observed = abacus.abacus(first, second)
    assert integers_only(observed)
    assert single_chars_only(observed)
    assert observed == expected

def test_04():
    """Test two digits with carry"""
    first = ['4', '2']
    second = ['1', '9']
    expected = ['6', '1']
    observed = abacus.abacus(first, second)
    assert integers_only(observed)
    assert single_chars_only(observed)
    assert observed == expected

def test_05():
    """Test uneven number of digits"""
    first = ['9', '2', '0']
    second = ['3', '1']
    expected = ['9', '5', '1']
    observed = abacus.abacus(first, second)
    assert integers_only(observed)
    assert single_chars_only(observed)
    assert observed == expected

def test_06():
    """Test uneven number of digits plus carry"""
    first = ['9', '2', '0']
    second = ['9', '1']
    expected = ['1', '0', '1', '1']
    observed = abacus.abacus(first, second)
    assert integers_only(observed)
    assert single_chars_only(observed)
    assert observed == expected

def test_07():
    """Test more uneven number of digits plus carry"""
    first = ['9', '9', '2', '0']
    second = ['9', '1']
    expected = ['1', '0', '0', '1', '1']
    observed = abacus.abacus(first, second)
    assert integers_only(observed)
    assert single_chars_only(observed)
    assert observed == expected

