## Replace all spaces in a string

Write a method to replace all spaces in a string with `‘%20’`. `O(n log n)`. (Gayle Laakmann, _Cracking the Coding Interview_, Ideas, 1.5)

    1. In Python, list comprehension can traverse string once and then use `join()` to reassemble into string:

            ''.join([i if i != ' ' else '%20' for i in s])

    Comment (Luu): Why is this `O(n lg n)`? I believe you can do that in linear time.
    
    Reply: Don't know why Laakman requests `O(n lg n)`. My solution is linear.

[end]