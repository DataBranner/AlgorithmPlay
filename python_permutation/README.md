## Permutation

Generate a list of all the permutations of an input list; return the permutations as a list of tuples.

There are recursive and dynamic (recursive with memoization) versions.

Run in repl as:

    import permutation as P
    P.permuations_recursive(the_list)
    P.permutations_dynamic(the_list)

for some list `the_list`.

As expected, the memoized version is much faster:

|  n  | non-memoized | memoized | ratio: memoized/non-memoized |
| --- | ------------ | -------- | ---------------------------- |
| 10 | 21.4 sec | 1.59 sec | 0.0743 |
| 9 | 1.95 sec | 140 msec | 0.0718 |
| 8 | 199 msec | 11.7 msec | 0.0588 |
| 7 | 23.5 msec | 1.38 msec | 0.0587 |
| 6 | 3.25 msec | 210 usec | 0.0646 |
| 5 | 497 usec | 43.1 usec | 0.0867 |
| 4 | 92.9 usec | 15.6 usec  | 0.168 |
| 3 | 20 usec | 7.63 usec | 0.382 |
| 2 | 4.86 usec | 4.54 usec | 0.934 |

In addition, I have supplied a different (unmemoized) version based on a piece of code by Becca Bainbridge. It does not return tuples, however.


[end]
