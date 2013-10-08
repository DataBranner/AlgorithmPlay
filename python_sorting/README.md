##  Sorting algorithms implemented in Python

I am trying to limit myself to basic Python tools, in order to study the structure of the algorithms. The `test` directory contains `py.test` tests comparing the output of my functions to the built-in Python sort. As will be seen in `test/test_sorting`, I am using a comprehension to generate lists of random integers for testing:

~~~
def fill_random_list(the_range=10000):
    return [random.randint(-100000, 100000) for i in range(the_range)]
~~~

 1. `mergesort`: takes about 4 ~ 4.5 times as long as built-in Python `sort()`.
 1. `quicksort`: takes about 2.3 times as log as built-in Python `sort()`.
 1. `insertionsort`: Timings are more interesting in this case.

 The timings with lists of random numbers look as though I'm getting quadratic time complexity:                      

 Timings for random lists:                                                      

        list cardinality: 100;   built-in sort: 228 usec;  insertionsort: 833 usec
        list cardinality: 1000;  built-in sort: 2.34 msec; insertionsort: 65.5 msec
        list cardinality: 10000; built-in sort: 24 msec;   insertionsort: 6.59 sec
        
        time : n ratio                                                              
        
            built-in sort: c.  10 : 10 — suggests linear time
            insertionsort: c. 100 : 10 — suggests O(n^2)

 For comparison, here are timings for lists of ascending vs. descending consecutive integers:            

        list cardinality: 100;   ascending: 61.5 usec; descending: 1.25 msec             
        list cardinality: 1000;  ascending: 649 usec;  descending: 125 msec              
        list cardinality: 10000; ascending: 6.46 msec; descending: 12.8 sec           
        
        time : n ratio
        
            ascending list (already in order): c.  10 : 10 — suggests linear time
            descending list (reverse order):   c. 100 : 10 — suggests quadratic time

 Time increases by a factor of 10 when n increases by a factor of 10; for the descending list, time increase by a factor of 100 when n increases by a factor of 10, quadratic time complexity for the known worst case.

 My `insertionsort` seems to be getting quadratic time with lists of random numbers.

[end]
