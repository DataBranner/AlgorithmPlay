# find_indices_summing_to_specified.py
# David Prager Branner
# 20131104, works.

"""Find pairs of elements of an array that sum to some specified value."""

def main(specified, array = None):
    """Assume that each element is unique in the array."""
    # Dispose of unusable cases.
    if not isinstance(array, list):
        return None
    # 1. Sort array.
    array.sort()
    # 2. Find list of differences for each index.
    differences = [specified - array[i] for i in range(len(array))]
    # 3. Math differences to original indices; each is a member of a pair.
    matches = set(array).intersection(differences)
    matches = sorted(list(matches))
    # 4. If matches is of odd length, middle index is half of 
    # 5. Find and return pairs, which are at opposite ends of sorted list.
    #    But if "matches" is of odd length, then middle index is half of
    #    "specified"; there is no corresponding value to make it reach
    #    "specified", so delete it by using "len(matches) // 2" below rather 
    #     than "len(matches) // 2 + 1"
    if matches:
        pairs = [(matches[i], matches[-(i+1)]) 
                for i in range(len(matches) // 2)]
        return pairs
