## Rotate a matrix 90°

Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees Can you do this in place? (Gayle Laakmann, _Cracking the Coding Interview_, Ideas, 1.6)

  1. The key to in-place solution is how the array is read as a matrix. Given


            matrix        array
            ------        -----
            20 21 22
            10 11 12  =>  00 01 02 10 11 12 20 21 22
            00 01 02      

  Here:

    * `N = 3`. 
    * Row `r` of matrix, given index `i` of array: `r` is `N` indices of the array, beginning at index `rN`. `r = i // N`.
    * Column `c` of the matrix is index `i` of the array, `c = i % N`. 
    * Index `i` of array, given row and column `r`, `c`, of matrix: `i = rN + c`.

  Now we want to convert the array into a _rotated_ matrix. We will rotate 90° counterclockwise.

            array                           matrix
            -----                           ------
                                            22 12 02
            00 01 02 10 11 12 20 21 22  =>  21 11 01
                                            20 10 00

  Now we recalculate the values for the various dimensions:

    * `N = 3`
    * Row `r` of matrix, given index `i` of array: `r = i % N`.
    * Column `c` of matrix, given index `i` of array: `c = N - (i // N)`.
    * Index `i` of array, given row and column `r`, `c`, of matrix: `i = N(N - 1 - c) + r`.

[end]