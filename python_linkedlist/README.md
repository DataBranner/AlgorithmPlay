## Python linked-list implementation

Use hash table.

Each key models a pointer, and is a randomly generated hex integer. Each value models a node and is implemented as a tuple containing (data, key_of_next_node).

Initialization requires at least one item in the list. Example:

    >>> import linkedlist as L
    >>> x = L.LinkedList(5)
    >>> x.print()
    5

Functions:

  1. `insert(datum[, prior_node])`: if `datum` is list or string, each index will be inserted into its own node of the linked list; otherwise, insertion is at the root. Returns key of inserted node.
  1. `delete(datum)`; returns deleted key of else `None`. On empty list, calls `destroy_on_empty()`.
  1. `find(datum)`. Returns key of found node or else `None`.
  1. `length()`
  1. `print(verbose = False)`: Prints whole list in a single line. On `verbose = True`, prints both key and data of each node on a successive line.
  1. `garbage_collect()`. On empty list, calls `destroy_on_empty()`.
  1. `return_list()`
  1. `destroy_on_empty()`: destroys `llist` and `root` to prevent further use of object. Used when `delete(datum)` or `garbage_collect()` produce an empty list.

Maybe no function for traversal — the cost of calling a function is expensive compared with implementing its content in place.

### Not yet done:

  * Test suite.
  * Option for doubly linked list using XOR.
  * Option for circular linked list.
  * `insert` at a particular index

[end]
