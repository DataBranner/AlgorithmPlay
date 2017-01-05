## Activity-Selection

After Cormen et al., _Introduction to Algorithms_, Third Edition, Chapter 16 "Greedy Algorithms", Section 16.1 "An activity-selection problem."

Two short functions, one recursive and one iterative, to find an ordered sequence (maximizing cardinality, but not considering total elapsed time) of activities that do not overlap: each activity is defined as a tuple `(start-time, finish-time)`.

The "trick" to the algorithm is that the input array of activities is sorted, in monotonically increasing order of finish-time. That sorting process enables the algorithm to ensure that, given any activity, no activities following it in the input array end earlier than it. Cormen's proof of the algorithm's validity is the most interesting part of the section.

### To use

 1. Set up virtual environment:

    ```bash
    python3.6 -m venv v_env3
    . v_env3/bin/activate
    pip install -R requirements_py3.txt
    ```

 2. Run tests:

    ```bash
    py.test test
    ```

 3. Unlike the Cormen originals, these are written to make use of Python's convenient lists, so the two functions only take a single input list as argument — no cursor is used in either the recursive or iterative version.

    The recursive version uses `collections.deque` to enable efficient `popleft`, until the deque has been emptied; the iterative version uses Python's `for item in items` syntax.

### Type hinting

There is a second of the code, named `activity_selector_typing.py`, which uses Python type hinting. The `mypy` program (installed from `requirements_py3.txt`, above) is a static type checker that reports no errors in this program.

```bash
mypy activity_selector_typing.py
```

I ran into problems when switching back and forth between `list` and `deque` in the context of `typing`. So for the typed version of the program, I have used lists alone, and am simply risking the added time complexity with `list.pop(0)` instead of `deque.popleft()` as in the untyped version.

[end]
