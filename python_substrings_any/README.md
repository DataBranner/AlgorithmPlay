## Substring search

Contains a single function:

    find_substring(pattern, target)

Returns `True` if `pattern` is found in `target`, otherwise returns `False`.

Arguments `pattern` and `target` must be non-zero and `target` must be at least as long as `pattern`.

### Strategy

To avoid searching for `pattern` within each successive appropriate-lengthed substring of `target`, compute the hash of the pattern and the hash of each successive appropriate-lengthed substring of `target`. Since `hash()` is computed in constant time, and there are at most `n - m + 1` comparisons (where `n = len(target)` and `m = len(pattern)`. So we expect O(n) running time.

### Timing results

Increasing the length of the target by a factor of 2 increases the running time by a factor of about 2, confirming linear time complexity.

However, Python's built-in substring search function (`str.find(substring)`) is far faster than linear time, as shown below.

#### Using `find_substring()`

~~~
n = 10: 10000 loops, best of 3: 71.3 usec per loop
n = 20: 10000 loops, best of 3: 124 usec per loop
n = 40:  1000 loops, best of 3: 230 usec per loop
n = 80:  1000 loops, best of 3: 461 usec per loop
n = 160: 1000 loops, best of 3: 942 usec per loop
n = 320:  100 loops, best of 3: 2.07 msec per loop
~~~

### Timeit code for `find_substring()`

~~~
python -m timeit -s '''
import random, string
import python_substrings_any as A
n = 10
the_targets = []
the_patterns = []
for i in range(100):
    the_targets.append("".join([random.choice(string.ascii_lowercase) for i in range(n)]))
    start_index = random.randint(0, n)
    stop_index = random.randint(start_index, n)
    if i < 50:
        the_patterns.append(the_targets[i][start_index:stop_index])
''' '''
for pattern, target in zip(the_patterns, the_targets):
    _ = A.find_substring(pattern, target)
'''
~~~


#### Using `target.find(pattern)`

~~~
n = 10: 100000 loops, best of 3: 13.1 usec per loop
n = 20: 100000 loops, best of 3: 13.7 usec per loop
n = 40: 100000 loops, best of 3: 14.5 usec per loop
n = 80: 100000 loops, best of 3: 16.4 usec per loop
n = 160: 10000 loops, best of 3: 19.4 usec per loop
n = 320: 10000 loops, best of 3: 26.4 usec per loop
~~~

### Timeit code for `target.find(pattern)`

~~~
python -m timeit -s '''
import random, string
import python_substrings_any as A
n = 320
the_targets = []
the_patterns = []
for i in range(100):
    the_targets.append("".join([random.choice(string.ascii_lowercase) for i in range(n)]))
    start_index = random.randint(0, n)
    stop_index = random.randint(start_index, n)
    if i < 50:
        the_patterns.append(the_targets[i][start_index:stop_index])
''' '''
for pattern, target in zip(the_patterns, the_targets):
    _ = target.find(pattern)
'''
~~~

[end]