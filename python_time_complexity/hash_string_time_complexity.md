## Time complexity of Python's hash function

Increasing by a factor of 10 the length of the string to be hashed does not increase the time of the process. That means the process is O(1).

### Timing results

For different lengths of the string to be hashed:

~~~
n = 10:     10000000 loops, best of 3: 0.0553 usec per loop
n = 100:    10000000 loops, best of 3: 0.0559 usec per loop
n = 1000:   10000000 loops, best of 3: 0.0632 usec per loop
n = 10000:  10000000 loops, best of 3: 0.0558 usec per loop
n = 100000: 10000000 loops, best of 3: 0.057 usec per loop
~~~

### Timing code

~~~
python -m timeit -s '''
import random, string, hashlib
n = 10
s = "".join([random.choice(string.ascii_lowercase) for i in range(n)])
''' '''
_ = hash(s)
'''
~~~

[end]
