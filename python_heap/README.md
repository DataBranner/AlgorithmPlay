## Naïve heap implementation

Contains
  
    heap_naive.py
    test/test_heap_naive.py

To create a heap use:

    the_heap = populate_tree(data)

where `data` is a list. To sort the data, use

    inorder_traverse(the_heap)

There are also functions

    preorder_traverse(the_heap)
    postorder_traverse(the_heap)
    breadfirst_traverse(the_heap)

Directory `test` is meant for use with `py.test`. 

### Strategy

  1. This implements a binary tree using node-objects. The heap invariant is always maintained, but insertions are done from the root down.
  2. There is no rebalancing, so it is possible create a heap with far too many levels — inefficient as a worst-case sorting tool.

[end]
