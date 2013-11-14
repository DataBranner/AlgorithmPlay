## Python linked-list implementation

Use hash table.

Each key models a pointer, and is a randomly generated hex integer. Each value models a node and is implemented as a tuple containing (data, key_of_next_node).

Initialization requires at least one item in the list. Example:

    >>> import linkedlist as L
    >>> x = L.LinkedList(5)
    >>> x.print()
    5

Functions:

  1. `insert(datum[, prior_node])`: if `datum` is list or string, each index will be inserted into its own node of the linked list.
  1. `delete(datum)`
  1. `find(datum)`
  1. `length()`
  1. `print(verbose = False)`: Prints whole list.
  1. `garbage_collect()`
  1. `return_list()`
  1. `destroy_on_empty()`: Used when `delete(datum)` or `garbage_collect()` produce an empty list.

Maybe no function for traversal — the cost of calling a function is expensive compared with implementing its content in place.

### Not yet done:

  * `insert_at_head()`.
  * Test suite.
  * Option for doubly linked list using XOR.
  * Option for circular linked list.

[end]
