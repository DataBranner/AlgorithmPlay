## Globbing (Global Wildcard Expansion)

Without turning to Python's regex tools, given an input string `s` and a glob pattern `p`, determine whether the pattern matches the whole string or not, returning `True` or `False`.

This program runs in Python3 and Python2.7. The glob syntax currently treated is

 * `?`: represents any single character
 * `*`: represents zero or more characters of any sort
 * `[abc]`: one character from among `a, b, c`
 * `[!abc]` or `[^abc]`: one character not from among `a, b, c`

### To run

Run `glob_match.py` using the module's `main` function:

    main(p, s)

where `p` is the glob pattern and `s` is the string to be matched. Below are examples of usage in Ipython:

```python
In [1]: import glob_match as G

In [2]: G.main('a?b', 'aab')     # ? can stand for 'a' in the string.
Out[2]: True

In [3]: G.main('a?b', 'abb')     # ? can stand for 'b' in the string.
Out[3]: True

In [4]: G.main('a??b', 'aab')    # ?? stands for 2 characters; there is only one.
Out[4]: False

In [5]: G.main('a*b', 'aab')     # * can stand for 'a' in the string.
Out[5]: True

In [6]: G.main('a*b', 'ababab')  # * can stand for 'baba' in the string.
Out[6]: True

In [7]: G.main('a?c', 'aab')     # There is no 'c' in the string.
Out[7]: False

In [8]: G.main('a[bfg]c', 'abc') # Character 'b' is found in the set [bfg].
Out[8]: True

In [9]: G.main('a[!fg]c', 'abc') # Character 'b' is not found in the set [bfg].
Out[9]: True

In [10]: G.main('a[^fg]c', 'abc') # Character 'b' is not found in the set [bfg].
Out[10]: True
```

There is a simpler version of the program, `glob_match_simple.py` that treats only the single-character wildcards, in directory `simple_version`. The same directory has another program, `glob_match_with_print.py`, that describes the decisions that are being made at each step for the simple version.

### Workings

 1. Uses two cursors to keep track of string indices, one for `p` and one for `s`.

 1. The pattern is sent initially to a lexer, `lexer.py`, which decides what function is to be applied to each element of the pattern. Here character sets (positive and negative) are gathered into a single unit.

 1. Dictionary-branching is used to send the strings and their cursors to various functions for matching. The branching dictionary is `actions` and it is populated based on the contents of `s` plus the `?` and `*` wildcards.

 1. Each function returns between zero and three cursor-pairs, which go into a queue `cursor_pair_queue` to be handled in order.

 1. Cursor-pairs are memoized in a dictionary `cursor_pairs_seen` to prevent repetition when `*` is encountered.

 1. The program returns `False` under two circumstances:

   2. a character is encountered in `p` that is not in `s`;
   2. there are no cursor-pairs left in the queue but either `p` or `s` has not yet been used up.

   Otherwise, the program return `True` when both cursors have reached the end of their respective strings.

### Testing

There is a Pytest suite in directory `test`.

### Other discussion

Python's own `glob` module relies on regex:

 * [glob.py](http://hg.python.org/cpython/file/3.4/Lib/glob.py) calls `fnmatch.filter()`
 * [fnmatch.py](http://hg.python.org/cpython/file/3.4/Lib/fnmatch.py) does the following:
   * converts a `glob` patthern regex (in `translate()`); 
   * compiles it and generates a `re.compile.match()` object (in `_compile_pattern()`);
   * calls the `re.compile.match()` object on various filenames (in `filter()`).

### Next features

 1. Eventually convert to Regex — see abandoned [regex engine](https://github.com/brannerchinese/regex_engine_py/) project.
 1. Add front-end visualization.

[end]
