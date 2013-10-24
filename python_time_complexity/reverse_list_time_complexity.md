## Time complexity of list.reverse()

Appears to be O(n): increasing _n_ by a factor of 10 leads to a time-increase of a factor of 10.

### Timings

~~~
n = 100: 10000 loops, best of 3: 120 usec per loop
n = 1000: 1000 loops, best of 3: 1.15 msec per loop
n = 10000: 100 loops, best of 3: 12.2 msec per loop
n = 100000: 10 loops, best of 3: 119 msec per loop
~~~

### Timeit code

~~~
python -m timeit -s '''
import random, string
n = 100000
''' '''
the_list = [random.choice(string.ascii_lowercase) for i in range (n)]
the_list.reverse()
'''
~~~

[end]