## FizzBuzz implementations

This directory contains three different implementations of FizzBuzz. The principle is to print the integers from 1 to 100, but to substitute "Fizz" for multiples of 3 and "Buzz" for multiples of 5; multiples of both 3 and 5 are replaced with "FizzBuzz".

 1. `fizzbuzz_procedural.py` is an ordinary procedural implementation. It has the slight wrinkle that it doesn't test for multiples of 15 explicitly but omits linefeed after "Fizz" until the "Buzz" condition has also been tested for.

 1. `fizzbuzz_single_string.py` combines all the output into a single string, multiplying each potential output item by a boolean and adding it to the output string. 

 1. `fizzbuzz_zip_cycles.py`, in an algorithm suggested by Joshua Bronson, uses `zip` to intersperse the output of "feeds" from generator-instantiations of the `itertools.cycle` method and `range`:

        from itertools import cycle
        
        def generate_feed(n, word):
            return [''] * (n - 1) + [word]
        
        for fizz, buzz, quack, foo, num in zip(
                cycle(generate_feed(3, 'Fizz')), 
                cycle(generate_feed(5, 'Buzz')), 
                range(1, 101)):
            print(fizz + buzz + quack + foo or num)

    This implementation is the most easily expanded. If, for instance, we wanted to replace not just multiples of 3 and 5 but any number of other integers, it would be simple to do so with minimal refactoring:

        from itertools import cycle
        
        def generate_feed(n, word):
            return [''] * (n - 1) + [word]
        
        for fizz, buzz, quack, foo, num in zip(
                cycle(generate_feed(3, 'Fizz')), 
                cycle(generate_feed(5, 'Buzz')), 
                cycle(generate_feed(7, 'Quack')), 
                cycle(generate_feed(11, 'Foo')), 
                range(1, 101)):
            print(fizz + buzz + quack + foo or num)

[end]
