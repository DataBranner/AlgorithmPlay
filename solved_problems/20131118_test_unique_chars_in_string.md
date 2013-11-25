## Test for unique characters in string

Implement an algorithm to determine if a string has all unique characters What if you can not use additional data structures? (Gayle Laakmann, _Cracking the Coding Interview_, Ideas, 1.1)

  1. Easy solution is quadratic: traverse list once; for each traversal, traverse the remainder and look for a duplicate.
  2. Sort copy of list; traverse, comparing adjacent items for duplication. `O(n log n)`, requires additional space.
  3. To avoid using additional space in above, can sort in place. However, that destroys original list.

[end]