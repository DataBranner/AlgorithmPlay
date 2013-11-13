## Time-cost of implementing simple operation as a function

It seems to be three and a half times faster not to add the overhead of a function call.

### Timings

~~~
python -m timeit -s """
def test(a, b):
    return a+b
a = 7
b = 16
""" """
_ = test(a, b)
"""

10000000 loops, best of 3: 0.104 usec per loop
~~~

~~~
python -m timeit -s """
a = 7
b = 16
""" """
_ = a + b
"""

10000000 loops, best of 3: 0.029 usec per loop
~~~

[end]