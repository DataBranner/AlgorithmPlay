## find_indices_summing_to_specified.py


### Problem

Given an array of unique elements, along with some specified value, find pairs of array elements that sum to the specified value.

### Solution

In order to avoid the quadratic-time solution of comparing every element in the array to every successive element, we first sort the array, which limits us to O(n log n). Other details are found in the comments.

### Functions

    main(specified, array)

`specified` is the value to which pairs of array elements must sum to.

There is also a small test suite in `test/`.

### Timing

Although I am expecting O(n log n) time complexity, timings with `timeit` seem to suggest linear complexity.

#### Timing results

~~~
n = 1000: 10000 loops, best of 3: 181 usec per loop
n = 2000:  1000 loops, best of 3: 383 usec per loop
n = 4000:  1000 loops, best of 3: 754 usec per loop
n = 8000:  1000 loops, best of 3: 1.56 msec per loop
n = 16000:  100 loops, best of 3: 3.22 msec per loop
~~~

#### Timing code

~~~
python -m timeit -s '''
import random
the_range = 16000
specified = the_range * 5
array = [random.randint(1, (the_range * 10)) for i in range(the_range)]
''' '''
array.sort()
differences = [specified - array[i] for i in range(len(array))]
matches = set(array).intersection(differences)
matches = sorted(list(matches))
if matches:
    pairs = [(matches[i], matches[-(i+1)])
            for i in range(len(matches) // 2)]
'''
~~~

[end]
