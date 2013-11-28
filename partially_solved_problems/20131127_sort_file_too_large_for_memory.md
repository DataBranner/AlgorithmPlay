## Sort file too large for memory

 * Using `with`, perform mergesort or quicksort, using temporary files instead of temporary subarrays. This would not be fast, however.

---

Three different solutions are discussed on [http://neopythonic.blogspot.com/2008/10/sorting-million-32-bit-integers-in-2mb.html](http://neopythonic.blogspot.com/2008/10/sorting-million-32-bit-integers-in-2mb.html):

 1. Mergesort, using more efficient methods of reading from and saving to disk.
 1. A "select range sort" proposed in the notes by Joel Hockey.
 1. Using the `memmap` method of Numpy (creates memory-map to an array on disk).

[end]