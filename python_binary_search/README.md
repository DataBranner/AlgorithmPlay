## Naïve binary search tree implementation

Contains
  
    binary_search_naive.py
    test/test_binary_search_naive.py

To create a tree use:

    the_tree = populate_tree(data)

where `data` is a list and `the_tree` is the root node of a tree, with subtrees nested within `node.left` and `node.right`. Each node also has a `key` and a `data` attribute, and a `parent` attribute for use in the `delete` function. Keys must be unique integers.

There is no rebalancing of the populated tree.

To sort the keys, use

    inorder_traverse(the_tree)

There are also functions

    preorder_traverse(the_tree)
    postorder_traverse(the_tree)
    breadfirst_traverse(the_tree)
    min(the_tree)
    max(the_tree)
    search(the_tree, to_find)
    delete(the_tree, to_delete)

whose names are self-explanatory. `to_find` and `to_delete` are keys.


Directory `test` is meant for use with `py.test`. 

### Strategy

  1. This implements a binary search tree using node-objects. The invariant

        node.left.key <= node.key <= node.right.key

  is always maintained.

  2. Insertions are done from the root down.
  2. There is no rebalancing, so it is possible create a tree with far too many levels — inefficient as a worst-case sorting tool.

### Timing

#### Populating a tree: 

  1. Average time complexity (randomly ordered list): O(n). 

  1. Worst-case time complexity (already sorted list): apparently O(n). 

#### In-order traversal: 

  1. Average time complexity (randomly ordered list): O(n). 

#### Data and timing code:

  1. Populating a tree: Average time complexity

        n: 10:  10000 loops, best of 3: 40.6 usec per loop.
        n: 100:  1000 loops, best of 3: 512 usec per loop;  factor increase: 12.7
        n: 1000:  100 loops, best of 3: 6.43 msec per loop; factor increase: 12.6
        n: 10000:  10 loops, best of 3: 80.2 msec per loop; factor increase: 12.5
        n: 100000: 10 loops, best of 3: 1.04 sec per loop;  factor increase: 13.0

  Timing code:

        python -m timeit -s '''
        import random
        import binary_search_naive as B
        n = 1000000
        def generate_list():
            return [random.randint(1, 10000000) for i in range(n)]
        ''' '''
        B.populate_tree(generate_list())
        '''

  2. Populating a tree: Worst-case time complexity

        n: 10:  10000 loops, best of 3: 21.5 usec per loop
        n: 100:  1000 loops, best of 3: 1.64 msec per loop
        n: 1000:  RuntimeError: maximum recursion depth exceeded in comparison

  Since recursion bottoms out, use smaller factor to increase _n_:

        n: 10:  10000 loops, best of 3: 21.5 usec per loop.
        n: 20:  10000 loops, best of 3: 71.9 usec per loop;  factor increase: 3.3
        n: 40:  1000 loops, best of 3: 272 usec per loop;  factor increase: 3.9
        n: 80:  1000 loops, best of 3: 1.04 msec per loop;  factor increase: 3.8
        n: 160: 100 loops, best of 3: 4.13 msec per loop;  factor increase: 4.0
        n: 320: 100 loops, best of 3: 16.9 msec per loop;  factor increase: 4.1
        n: 640: 10 loops, best of 3: 69.2 msec per loop;  factor increase: 4.1

  Timing code:

        python -m timeit -s '''
        import random
        import binary_search_naive as B
        n = 640
        def generate_list():
            return [i for i in range(n)]
        ''' '''
        B.populate_tree(generate_list())
        '''

  3. In-order traversal: Average time complexity

        n: 10:  10 loops, best of 100: 5.36 usec per loop.
        n: 20:  10 loops, best of 100: 10.5 usec per loop
        n: 40:  10 loops, best of 100: 20 usec per loop
        n: 80:  10 loops, best of 100: 40.8 usec per loop
        n: 160: 10 loops, best of 100: 76.8 usec per loop
        n: 320: 10 loops, best of 100: 155 usec per loop
        n: 640: 10 loops, best of 100: 324 usec per loop

  Timing code:

        python -m timeit -r 100 -n 10 -s '''
        import random
        import binary_search_naive as B
        n = 640
        def generate_list():
            return [random.randint(1, 10000000) for i in range(n)]
        x = B.populate_tree(generate_list())
        ''' '''
        _ = B.inorder_traverse(x)
        '''

[end]
