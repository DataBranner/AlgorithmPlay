## python_substrings

Exercises involving substring search.

### Task

Given an input string `s`, find  example of the longest substring containing no more than some prescribed maximum number of unique characters.

### To use

There are two different versions of the program:

  * `substrings_set_and_list.py`
  * `substrings_list_only.py`

With input string `s` and optional prescribed maximum number of unique characters `max_uniq`, the function:

    find_substring(s, max_uniq = 2)

returns the longest substring (or the first-found longest substring, if there is more than one of this length) with two unique characters (or some other prescribed maximum number).

There is also a function 

    test_random(length = 100, max_uniq = 2)

that generates a random string of prescribed length and then asks whether more than the prescribed number of unique characters appears in the longest substring returned by `find_substring()`. If not, the longest substring is returned, alone; but if so, the number of unique characters actually found is also reported.

### Strategy

  1. Input: 
    1. `s`: the string
    1. `max_uniq`: (optional) the prescribed maximum number of unique characters.
  2. Keep track of the longest acceptable running substring, and also the longest of any substring found. When the running substring exceeds the longest, replace the longest with it. 
  3. Substrings are represented merely as their starting and ending indices in the original input string `s`, rather than as string datatypes proper, which are slower to manipulate. The start- and end-indices of the running and longest substrings found are stored in.
    1.  start_i_longest
    2.  end_i_longest
    3.  start_i_running
    4.  end_i_running
  1. Traverse the characters input string `s` once.
  1. Each newly encountered character is added to a list `chars_found`, so that there is a running list of these characters. 
  1. If a character is not new, it is added directly to the running substring and traversal of the input string continues. If a character is new, however, we must find out whether `max_uniq` has been exceeded or not. Keeping track of the number of unique characters in the running substring is done in two different ways in the two different versions of the program. 
    1. In `substrings_set_and_list.py`, newly encountered characters are also added to a set `unique_running`.
    1. In `substrings_list_only.py`, the list `chars_found` is used for this purpose.
  1. Sets can be searched on average in constant time to determine whether a character is "newly encountered" or not; lists are searched on average in linear time. Since this search takes place once for each character traverse in the input string, potentially it can lead to the program running in quadratic time. Now, unless the input string and `max_uniq` are both relatively large, the linear searching time does not cause problems. Timing results are reported later in this document.
  3. When the number of unique characters in the current running substring exceeds `max_uniq`, the current substring is abandoned and a new one is begun. This is done in slightly different ways in the two versions of the program. 
    1. In `substrings_set_and_list.py`, we remove from `unique_running` that element added longest ago. But before proceeding we need to check whether that character reappears later in the next running substring. One way to do this would be to search the running substring itself for the character in question, but that is a linear-time operation that, within the original linear-time traversal of the input string, would give us quadratic time. Instead, we turn to `chars_found`, using a cursor (`cursor`) to step through it index by index, until `cursor` points to an index not more than `max_uniq` from the current end of the list. Although stepping through the list is linear, it is done in parallel to stepping through the input string, = 𝓞(2n) ∈ 𝓞(n).
    1. In `substrings_list_only.py`, `cursor` alone can be used with `chars_found`, and there is no need to remove any characters from any containers.
  1. At the end of the traversal of `s`, the longest substring found is reported.    
    
### Test suite

Thirteen tests are supplied for each program. Change to directory `test` and run `py.test`.

### Timing

Based on timings using sufficiently large input strings, `strings_set_and_list.py` appears to run in linear time regardless of the values of `s` and `max_uniq`, while `substrings_list_only.py` runs in considerably more than linear time with sufficiently large values of `s` and `max_uniq`.

#### Results

Random string's length and time to complete:

##### For max_uniq = 2

| length of `s` |  List only: time of loop   |   List only: Δ`s`/ Δ time   |     |  Set & list: time of loop   | Set & list: Δ`s`/ Δ time   |
| ------------:|:------------:|:------------:| --- |:------------:|:------------:|
|          100 |    207 usec  |      —       |     |    218 usec  |      —       |
|         1000 |   1.83 msec  |     0.88     |     |   2.11 msec  |     0.97     |
|        10000 |   18.5 msec  |     1.01     |     |   21.8 msec  |     0.98     |
|       100000 |    187 msec  |     1.01     |     |    222 msec  |     1.02     |
|      1000000 |   1.92 sec   |     1.03     |     |    2.18 sec  |     0.98     |

##### For max_uniq = 10

| length of `s` |  List only: time of loop   |   List only: Δ`s`/ Δ time   |     |  Set & list: time of loop   | Set & list: Δ`s`/ Δ time   |
| ------------:|:------------:|:------------:| --- |:------------:|:------------:|
|          100 |    222 usec  |      —       |     |    220 usec  |      —       |
|         1000 |    1.9 msec  |     0.86     |     |   2.08 msec  |     0.94     |
|        10000 |   18.8 msec  |     0.99     |     |   21.6 msec  |     1.04     |
|       100000 |    188 msec  |     1.00     |     |    225 msec  |     1.04     |
|      1000000 |    1.93 sec  |     1.03     |     |     2.3 sec  |     1.02     |

##### For max_uniq = 100

| length of `s` |  List only: time of loop   |   List only: Δ`s`/ Δ time   |     |  Set & list: time of loop   | Set & list: Δ`s`/ Δ time   |
| ------------:|:------------:|:------------:| --- |:------------:|:------------:|
|         1000 |   3.28 msec  |      —       |     |   1.81 msec  |      —       |
|        10000 |    126 msec  |     3.84     |     |   17.9 msec  |     0.99     |
|       100000 |    11.5 sec  |     9.13     |     |    180 msec  |     1.01     |
|      1000000 | 1.82e+03 sec |  158.27      |     |    1.81 sec  |     1.00     |

##### For max_uniq = 1000

| length of `s` |  List only: time of loop   |   List only: Δ`s`/ Δ time   |     |  Set & list: time of loop   | Set & list: Δ`s`/ Δ time   |
| ------------:|:------------:|:------------:| --- |:------------:|:------------:|
|        10000 |    129 msec  |      _       |     |   16.5 msec  |      _       |
|       100000 |    11.9 sec  |     9.22     |     |    172 msec  |     1.04     |

Using a list only is slightly faster than using a list and a set until the values of `s` and `max_uniq` become relatively large.

#### Sample timeit code

~~~
python -m timeit -s '''
import substrings
import random
import string
max_uniq = 100''' '''
s = "".join([random.choice(string.ascii_uppercase) for i in range(10)])
result = substrings.find_substring(s, max_uniq)'''
~~~

[end]
