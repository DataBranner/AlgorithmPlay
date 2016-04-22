"""Use normal Python methods to solve by actual addition."""

def abacus(first, second):
    first = ''.join(first)
    second = ''.join(second)
    the_sum = str(int(first) + int(second))
    return [char for char in the_sum]
