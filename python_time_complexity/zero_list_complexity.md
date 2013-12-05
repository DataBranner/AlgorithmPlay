## Timing comparison: two ways to zero a Python list of fixed length

### Methods

 1. `[None] * cardinality`
 2. `[None for i in range(cardinality)]`

Both return in linear time, but the former is significantly faster.

### Timeit tabulated results

**Using `[None] * cardinality`**

| cardinality | time per loop | factor increase, t/cardinality |
| -----------:| -------------:|:------------------------------:|
| 100 | 0.445 usec | — |
| 1000 | 2.25  usec | 0.51 |
| 10000 | 21.8  usec | 0.97 |
| 100000 | 227  usec | 1.0 |
| 1000000 | 2.51  msec | 1.1 |
| 10000000 | 44   msec | 1.8 |
| 100000000 | 496  msec | 1.1 |

**Using `[None for i in range(cardinality)]`**

| cardinality | time per loop | factor increase, t/cardinality |
| -----------:| -------------:|:------------------------------:|
| 100 | 4.08  usec | — |
| 1000 | 35.3  usec | 0.87 |
| 10000 | 331  usec | 0.94 |
| 100000 | 3.71  msec | 1.1 |
| 1000000 | 37.8  msec | 1.0 |
| 10000000 | 380  msec | 1.0 |
| 100000000 | 3.7   sec | 1.0 |

### Timeit code and raw results

~~~
python -m timeit '''_ = [None] * cardinality'''

cardinality = 100: result: 1000000 loops, best of 3: 0.445 usec per loop
cardinality = 1000: result: 100000 loops, best of 3: 2.25 usec per loop
cardinality = 10000: result: 10000 loops, best of 3: 21.8 usec per loop
cardinality = 100000: result: 1000 loops, best of 3: 227 usec per loop
cardinality = 1000000: result: 100 loops, best of 3: 2.51 msec per loop
cardinality = 10000000: result: 10 loops, best of 3: 44 msec per loop
cardinality = 100000000: result: 10 loops, best of 3: 496 msec per loop

python -m timeit '''_ = [None for i in range(cardinality)]'''

cardinality = 100: result: 100000 loops, best of 3: 4.08 usec per loop
cardinality = 1000: result: 10000 loops, best of 3: 35.3 usec per loop
cardinality = 10000: result: 1000 loops, best of 3: 331 usec per loop
cardinality = 100000: result: 100 loops, best of 3: 3.71 msec per loop
cardinality = 1000000: result: 10 loops, best of 3: 37.8 msec per loop
cardinality = 10000000: result: 10 loops, best of 3: 380 msec per loop
cardinality = 100000000: result: 10 loops, best of 3: 3.7 sec per loop
~~~
