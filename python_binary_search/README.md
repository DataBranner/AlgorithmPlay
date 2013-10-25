## Naïve binary search tree implementation

Contains
  
    binary_search_naive.py
    test/test_binary_search_naive.py

To create a tree use:

    the_tree = populate_tree(data)

where `data` is a list. To sort the data, use

    inorder_traverse(the_tree)

There are also functions

    preorder_traverse(the_tree)
    postorder_traverse(the_tree)
    breadfirst_traverse(the_tree)

Directory `test` is meant for use with `py.test`. 

### Strategy

  1. This implements a binary search tree using node-objects. The invariant —

    node.left.key <= node.key <= node.right.key

— is always maintained.

  2. Insertions are done from the root down.
  2. There is no rebalancing, so it is possible create a tree with far too many levels — inefficient as a worst-case sorting tool.

### Timing

Average time complexity: O(n). Data and timing code below:

~~~
n: 10:  10000 loops, best of 3: 40.6 usec per loop.
n: 100:  1000 loops, best of 3: 512 usec per loop;  factor increase: 12.7
n: 1000:  100 loops, best of 3: 6.43 msec per loop; factor increase: 12.6
n: 10000:  10 loops, best of 3: 80.2 msec per loop; factor increase: 12.5
n: 100000: 10 loops, best of 3: 1.04 sec per loop;  factor increase: 13.0
~~~

~~~
python -m timeit -s '''
import random
import binary_search_naive as B
n = 1000000
def generate_list():
    return [random.randint(1, 10000000) for i in range(n)]
''' '''
B.populate_tree(generate_list())
'''
~~~

[end]
