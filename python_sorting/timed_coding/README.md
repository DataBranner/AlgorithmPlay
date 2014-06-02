## Timed Coding of Python Sorts

 * 20140601: 
   * mergesort. All complete in 29 minutes, including test suite. Most time wasted: when one list is used up, must extend `combined` by the *remainder* of the other list, not the whole other list. Another stupid mistake: forgot that `int1 / int2` is not floor division in Python3; need `int1 // int2` for that.
   * insertionsort. All complete in 8 minutes, including test suite. No errors.


[end]
