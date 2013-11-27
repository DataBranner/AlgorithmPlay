## Find kth-largest integer in file too large to sort

Given a file of integers, too large to be sorted in memory, find the kth-largest element.

 * Use set `the_set` to hold up to `k` values.
 * Assume we ignore ties.
 * Use variable `min_in_set` to remember smallest value in `the_set`.
 * As you traverse the file, keep only the highest `k` elements found; compare each new element with the lowest of these, in `min_in_set`. If it is higher, remove `min_in_set` and add the new element to `the_set`.

~~~
def k_smallest(k, filename):
    the_set = set()
    min_in_set = None
    with open(filename) as f:
        while f:
            elem = f.readline()
            if not elem: # needed because end of file is \n
                break
            elem = int(elem[:-1]) # needed because end of line is \n
            if len(the_set) < k:
                the_set.add(elem)
                min_in_set = min(the_set)
            elif elem > min_in_set:
                the_set.remove(min_in_set)
                the_set.add(elem)
                min_in_set = min(the_set)
    return min_in_set
~~~

Generate large file to test:

~~~
import random, sys
with open('large_int_file', 'w') as f:
    f.write('\n'.join(
            [str(random.randint(0, sys.maxsize)) for i in range(10**5)]))
~~~

With a much larger file than this — too large to retain in memory as a string — we could append values using `open('large_int_file', 'a')`.

[end]