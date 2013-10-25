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

[end]
