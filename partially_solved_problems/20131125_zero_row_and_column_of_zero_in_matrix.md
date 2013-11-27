## Zero the row and column of any matrix element that has value 0

Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0. (Gayle Laakmann, _Cracking the Coding Interview_, Ideas, 1.7)

  * This must mean that we first find all of the zeroes and then modify each affected row and column. After the first such modification, all rows and columns would have a zero and so on a second pass the whole matrix would have to be zeroed, which seems an unlikely goal. So we have to separate the checking for zeroes from the modification of affected rows and columns.
  * We would like to avoid modifying any element more than once, for efficiency's sake. We can do this by storing each row and column to be modified in a set, avoiding redundancy.

[end]