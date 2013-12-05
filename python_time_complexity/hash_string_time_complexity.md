## Time complexity of Python's hash function

Increasing by a factor of 10 the length of the string to be hashed increases by a factor of 10 the time of the process. That means the process is O(n).

### Timing results

For different lengths of the string to be hashed:

~~~
length: 10: 100000 loops, best of 3: 14.4 usec per loop
length: 100: 10000 loops, best of 3: 117 usec per loop
length: 1000: 1000 loops, best of 3: 1.12 msec per loop
length: 10000: 100 loops, best of 3: 11.1 msec per loop
length: 100000: 10 loops, best of 3: 112 msec per loop
~~~

### Timing code

~~~
python -m timeit -s '''
import random, string
n = 100000
''' '''
s = "".join([random.choice(string.ascii_lowercase) for i in range(n)])
_ = hash(s)
'''
~~~

[end]