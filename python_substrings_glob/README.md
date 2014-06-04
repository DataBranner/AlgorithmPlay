## Python Substrings Problems: Globbing (Global Wildcard Expansion)

Without turning to Python's regex tools, given an input string `s` and a glob pattern `p`, determine whether the pattern matches the whole string or not, returning `True` or `False`.

This program runs in Python3 and Python2.7. The glob syntax currently treated is

 * `?`: represents any single character
 * `*`: represents zero or more characters of any sort

### To run

Run using the module's `main` function:

    main(p, s)

where `p` is the glob pattern and `s` is the string to be matched. Below are examples of usage in Ipython:

```python
In [1]: import glob_match as G

In [2]: G.main('a?b', 'aab')    # ? can stand for 'a' in the string.
Out[2]: True

In [3]: G.main('a?b', 'abb')    # ? can stand for 'b' in the string.
Out[3]: True

In [4]: G.main('a??b', 'aab')   # ?? stands for 2 characters; there is only one.
Out[4]: False

In [5]: G.main('a*b', 'aab')    # * can stand for 'a' in the string.
Out[5]: True

In [6]: G.main('a*b', 'ababab') # * can stand for 'baba' in the string.
Out[6]: True

In [7]: G.main('a?c', 'aab')    # There is no 'c' in the string.
Out[7]: False
```

### Workings

 1. Uses two cursor to keep track of string indices, one for `p` and one for `s`.

 1. Dictionary-branching is used to send the strings and their cursors to various functions for matching. The branching dictionary is `actions` and it is populated based on the contents of `s` plus the `?` and `*` wildcards.

 1. Each function returns between zero and three cursor pairs, which go into a queue `cursor_pair_queue` to be handled in order.

 1. Cursor-pairs are memoized in a dictionary `cursor_pairs_seen` to prevent repetition when `*` is encountered.

 1. The program returns `False` under two circumstances:

   2. a character is encountered in `p` that is not in `s`;
   2. there are no cursor-pairs left in the queue but either `p` or `s` has not yet been used up.

   Otherwise, the program return `True` when both cursors have reached the end of their respective strings.

### Testing

There is a test suite in directory `test`.

[end]
