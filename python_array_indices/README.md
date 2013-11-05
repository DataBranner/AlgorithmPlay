## find_indices_summing_to_specified.py


### Problem

Given an array of unique elements, plus some specified value, find pairs of array elements that sum to the specified value.

### Solution

In order to avoid the quadratic-time solution of comparing every element in the array to every successive element, we first sort the array, which limits us to O(n log n). Other details are found in the comments.

### Functions

    main(specified, array)

`specified` is the value to which pairs of array elements must sum to.

There is also a small test suite in `test/`.

[end]
