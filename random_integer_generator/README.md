## Simulate random integer generator

Problem: Given a function that produces a random integer between 1 and some value _m_, write a function that produces a random integer between 1 and some other value _n_.

Solution: Generate the sum of "desired" number of 1-to-"given" random numbers
and then find the modulus remainder; add 1 to make the range of results begin
at 1.

This directory contains a program `simulate_random_range.py` containing the function 

    main(given, desired)

where `given` is _m_ in the description above and `desired` is _n_. There is also a second function, `comprehension()` that performs the same computation but does so as a list comprehension rather than a for-loop; this function turns out to be slower than `main()`.

The directory also contains a program `test_randomness_simulate_random_range.py`, whose function 

    main(trials=100, given=5, desired=7)

returns the ratio of standard deviation to mean for our simulated function and the actual results of random.randint(1, desired), as well as the the proportion of these two ratios, which we predict never to be further apart than 1:3.

There is also a `py.test` test in a `test/` directory, which asserts the 1:3 bound.

[end]
