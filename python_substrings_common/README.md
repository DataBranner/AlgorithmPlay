## Find longest common substrings in a group of input strings

### To use

Function

    find_longest_common_substring(n=100, num_strings=2, strings=[], all=True)

returns a list of longest common substrings. Parameters:

  * `num_strings` specifies how many input strings there are; this is useful because if parameter `strings` is left blank, the program will generate random strings, of length `n`. 
  * `all` allows the user to choose whether all common substrings of the greatest length found will be returned, or just one example.

There is also a function

    find_all_substrings(s, non_empty=True)

which returns all distinct substrings of a given input string `s`. The parameter `non_empty` allows the user to specify whether the empty string `''` is included.

### Strategy

The program `find_longest_common_substring_brute_force.py` uses brute force: it calculates all the possible substrings of all the input strings, and then returns their intersection.

### Testing

No tests have been prepared yet.

[end]
