## Reverse C-style string

Write code to reverse a C-Style String (C-String means that “abcd” is represented as five characters, including the null character.) (Gayle Laakmann, _Cracking the Coding Interview_, Ideas, 1.2)

  1. Traverse list, doing the following steps: hold address of `next_node`; change `next_node` attribute to the previous nodes's `next_node`, which you have been holding; insert `null` at root and delete from tail; set rootpointer to address of former last node.
  1. Use XOR doubly linked list?

[end]