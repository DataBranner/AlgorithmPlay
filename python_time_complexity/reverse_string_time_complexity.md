## Time complexity of reversing a python string

Using the simple built-in slicing form of string reversal: `the_string[::-1]`.

A ten-fold increase in string-length corresponds to a ten-fold increase in running time, which suggests O(n) complexity. 

### Timing data

~~~
Time for increasing string lengths:
length = 10:  1000000 loops, best of 3: 0.131 usec per loop
length = 100: 1000000 loops, best of 3: 0.33 usec per loop
length = 1000: 100000 loops, best of 3: 2.36 usec per loop
length = 10000: 10000 loops, best of 3: 22.3 usec per loop
length = 100000: 1000 loops, best of 3: 223 usec per loop
length = 1000000: 100 loops, best of 3: 2.29 msec per loop
length = 10000000: 10 loops, best of 3: 22.5 msec per loop
~~~

### Timing code

~~~
python -m timeit -s '''
import random
import string
the_string = "".join([random.choice(string.ascii_letters) for i in range(10)])
''' '''
_ = the_string[::-1]
'''
~~~

[end]
