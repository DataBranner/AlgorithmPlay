## Is n an integer power of k?

Given integers `n` and `k`, determine if `n` is an integer power of `k`.

Python 3 pseudocode:
~~~
def is_int_power(n, k):
    if n < k:
        return False
    temp = n
    while temp > k:
        if temp % k:
            return False
        temp /= k
    return True
~~~

Bug: with large values, this function fails. Example:

    In [3]: is_int_power(79**50, 79)
    Out[3]: False

I think this has something to do with accumulating floating point error. Substituting floor division fixes that result:

~~~
def is_int_power(n, k):
    if n < k:
        return False
    temp = n
    while temp > k:
        if temp % k:
            return False
        temp //= k
    return True
~~~
Output:
    In [6]: is_int_power(79**999, 79)
    Out[6]: True
    
    In [7]: is_int_power(79**999 + 1, 79)
    Out[7]: False



[end]