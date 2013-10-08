##  Hash table implemented in Python

I am limiting myself to basic Python tools, in order to study the structure of the algorithms without turning to implementations of those same algorithms. 

### Programs

  1. `hash_table.py`: Models a hash table using an array (rather than a dictionary, which in Python is a hash table). The table uses chaining when collisions occur.
 
  Two kinds of tables can be created, with a default initial size of 16 slots:

   * non-resizeable:

        import hash_table
        ht = hash_table.Hash_Table()
        # To create a different number of slots from the default use:
        # ht = hash_table.Hash_Table(size)

   * resizeable:

        import hash_table
        ht = hash_table.Hash_Table(resizeable=True)
        # To create a different number of slots from the default use:
        # ht = hash_table.Hash_Table(size, True)

  In the latter, the table will be resized by a factor of 2 (default; can be controlled by setting `self.resize_factor`) when the number of filled slots exceeds the value `self.resize_threshold` (default is `size / 2`),
  
  Main functions:
  
   * `insert(key, value, the_hash=None)`
   * `retrieve(key)`
    
  There are also functions `insert_collis` and `retrieve_collis` for internal use when a slot contains collisions, and `resize` for expanding the number of slots when necessary.
  
  Because the built-in function produces hashes that may be positive or negative, I double the chances of collision. I could avoid this by adding `sys.maxsize` before hashing, but that would cost time converting to a long integer.
  
  1. `test/` contains `py.test` tests. 

### Timing issues

The different time complexity of the hash table with and without resizing is illustrated in the `timeit` results below. Resizing has a one-time cost, `O(n)`, but that cost is "amortized" over the life of the resized table, whose retrieval time remains approximately constant. 

The value in column `time increase / Δn` is constant in neither case (without vs. with resizing), but it is much closer to being constant in the latter case.

#### W/o resizing ( table created as `ht = hash_table.Hash_Table(size)` )

| 									   | timeit data           | time				           | (this timing/last timing) / Δn |
| ----------- | --------------------- | ------------------ | ----------------------------- |
| n = 10      | 1000 loops, best of 3 | 242 usec per loop 	|                               |
| n = 100     | 1000 loops, best of 3 | 475 usec per loop	 | 0.196                         |
| n = 1000    | 100 loops, best of 3  | 4.85 msec per loop	| 1.02                          |
| n = 10000   | 10 loops, best of 3   | 282 msec per loop	 | 5.81                          |
| n = 100000  | 10 loops, best of 3   | 52.3 sec per loop 	| 18.5                          |

#### W/  resizing ( table created as `ht = hash_table.Hash_Table(size, True)` )

| 									   | timeit data           | time				           | (this timing/last timing) / Δn |
| ----------- | --------------------- | ------------------ | ----------------------------- |
| n = 10      | 1000 loops, best of 3 | 246 usec per loop		|                               |
| n = 100     | 1000 loops, best of 3 | 674 usec per loop	 | 0.274                           |
| n = 1000    | 100 loops, best of 3  | 4.29 msec per loop | 0.636                           |
| n = 10000   | 10 loops, best of 3   | 37.1 msec per loop | 0.865                           |
| n = 100000  | 10 loops, best of 3   | 663 msec per loop	 | 1.79                            |

The `timeit` code used was as follows:

~~~
python -m timeit -s '''
import hash_table as hash_table
import random
import string
def random_key(the_range=8): 
    return "".join([random.choice(string.ascii_letters) 
            for i in range(the_range)])
dictionary = {random_key() : random.randint(-1000, 1000) for i in range(10)}
def test_insert_retrieve():
    size = 16
    ht = hash_table.Hash_Table(size)
    _ = [ht.insert(item, dictionary[item]) for item in dictionary]
    for trial in range(25):
        test_key = random.sample(dictionary.keys(), 1)[0]
        assert ht.retrieve(test_key) == dictionary[test_key]''' '''
test_insert_retrieve()'''

~~~

Different values of n are placed in the range() function in the line:

    dictionary = {random_key() : random.randint(-1000, 1000) for i in range(10)}

### Occasional error in the code with `timeit`

Possible error:

A couple of times I have had an error occur when using `timeit` with the code above:

~~~
$ python -m timeit -s '''
> import hash_table as hash_table
> import random
> import string
> def random_key(the_range=8): 
>     return "".join([random.choice(string.ascii_letters) 
>             for i in range(the_range)])
> dictionary = {random_key() : random.randint(-1000, 1000) for i in range(100000)}
> def test_insert_retrieve():
>     size = 16
>     ht = hash_table.Hash_Table(size, True)
>     _ = [ht.insert(item, dictionary[item]) for item in dictionary]
>     for trial in range(25):
>         test_key = random.sample(dictionary.keys(), 1)[0]
>         assert ht.retrieve(test_key) == dictionary[test_key]''' '''
> test_insert_retrieve()'''
Traceback (most recent call last):
  File "/usr/local/Cellar/python3/3.3.2/Frameworks/Python.framework/Versions/3.3/lib/python3.3/timeit.py", line 313, in main
    r = t.repeat(repeat, number)
  File "/usr/local/Cellar/python3/3.3.2/Frameworks/Python.framework/Versions/3.3/lib/python3.3/timeit.py", line 218, in repeat
    t = self.timeit(number)
  File "/usr/local/Cellar/python3/3.3.2/Frameworks/Python.framework/Versions/3.3/lib/python3.3/timeit.py", line 190, in timeit
    timing = self.inner(it, self.timer)
  File "<timeit-src>", line 21, in inner
    test_insert_retrieve()
  File "<timeit-src>", line 17, in test_insert_retrieve
    assert ht.retrieve(test_key) == dictionary[test_key]
  File "./hash_table.py", line 46, in retrieve
    return self.array[index][1]
TypeError: 'NoneType' object is not subscriptable
$
~~~

and

~~~
$ python -m timeit -s '''
> import hash_table as hash_table
> import random
> import string
> def random_key(the_range=8): 
>     return "".join([random.choice(string.ascii_letters) 
>             for i in range(the_range)])
> dictionary = {random_key() : random.randint(-1000, 1000) for i in range(500)}
> def test_insert_retrieve():
>     size = 16
>     ht = hash_table.Hash_Table(size, True)
>     _ = [ht.insert(item, dictionary[item]) for item in dictionary]
>     for trial in range(25):
>         test_key = random.sample(dictionary.keys(), 1)[0]
>         assert ht.retrieve(test_key) == dictionary[test_key]''' '''
> test_insert_retrieve()'''
Traceback (most recent call last):
  File "/usr/local/Cellar/python3/3.3.2/Frameworks/Python.framework/Versions/3.3/lib/python3.3/timeit.py", line 304, in main
    x = t.timeit(number)
  File "/usr/local/Cellar/python3/3.3.2/Frameworks/Python.framework/Versions/3.3/lib/python3.3/timeit.py", line 190, in timeit
    timing = self.inner(it, self.timer)
  File "<timeit-src>", line 21, in inner
    test_insert_retrieve()
  File "<timeit-src>", line 17, in test_insert_retrieve
    assert ht.retrieve(test_key) == dictionary[test_key]
  File "./hash_table.py", line 46, in retrieve
    return self.array[index][1]
TypeError: 'NoneType' object is not subscriptable
$
~~~

I rewrote the `retrieve()` function with an `elif` block to catch errors of this kind:

~~~
def retrieve(self, key):                              
    '''Retrieves the value associated with a desired unique key.'''
    the_hash = hash(key)                              
    index = the_hash % self.size                      
    if isinstance(self.array[index], list):           
        return self.retrieve_collis(index, key)       
    elif self.array[index] == None:                   
        print('searching for', key, 'at index', index, 'in array', array)   
        sys.exit(0)                
    else:                          
        return self.array[index][1]                   
~~~

And then ran 50M trials of the function:

~~~
import random
import string
import hash_table

def random_key(the_range=8):
    '''Generate string of random ASCII letters for use as random key.'''
    return ''.join([random.choice(string.ascii_letters)
            for i in range(the_range)])

# Fill dictionary with random keys and values.
dictionary = {random_key() : random.randint(-1000, 1000) for i in range(1000)}

def test_insert_retrieve():
    '''Test retrieval of inserted items.'''
    size = 16
    ht = hash_table.Hash_Table(size)
    counter = 0
    # Use dictionary to populate hash table.
    _ = [ht.insert(item, dictionary[item]) for item in dictionary]
    # Test by comparing individual items.
    while True:
        counter += 1
        test_key = random.sample(dictionary.keys(), 1)[0]
        assert ht.retrieve(test_key) == dictionary[test_key]
        print(counter, 'complete without errors')
~~~

but the error did not occur. I conclude that it is an artefact of `timeit`.

[end]
