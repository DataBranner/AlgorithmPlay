# abacus.py
# This solution by Leslie Klein as an interview practice problem on 20160421.

"""Model addition on an abacus.

Input:  two lists of strings;
Output: one list of strings.

>>> abacus(['3'], ['5'])
['8']

All strings are one-character-length integers.
"""

def abacus(first=['3'], second=['5']):
    """Return a list containing the digit-by-digit sum of the input lists."""
    # TODO: rewrite the rest of this function

    # Get the arrays to be the same size.
    nf = len(first)
    ns = len(second)
    diff = nf - ns
    if diff < 0:
        first = [0] * -diff + first
    else:
        second = [0] * diff + second

    # Reverse both lists for ease of addition.
    first = first[::-1]
    second = second[::-1]

    # Decide whether we need to carry a 1 or not, for each digit.
    c = 0
    sums = []
    for a, b in zip(first, second):
        # Convert string-elements to ints.
        a, b = int(a), int(b)
        s = a + b + c
        c = 1 if s > 9 else 0
        sums.append(s%10)
    sums = sums[::-1]
    sums = ([1] + sums) if c else sums


    return [str(i) for i in sums]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
