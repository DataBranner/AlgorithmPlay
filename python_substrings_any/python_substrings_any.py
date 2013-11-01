# python_substrings_any.py
# David Prager Branner
# 20131101

def find_substring(pattern, target):
    """Search by comparing hashes of pattern and successive substrings."""
    # Eliminate trivial cases.
    n = len(target)
    m = len(pattern)
    if (not n or not m or m > n):
        return False
    #
    # Search by comparing hashes.
    pattern_hash = hash(pattern)
    for string_start in range(n - m + 1):
        string_end = string_start + m
        if pattern_hash == hash(target[string_start:string_end]):
            return True
    return False
