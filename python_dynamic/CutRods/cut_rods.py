# cut_rods.py
# David Prager Branner
# 20131209, does not work
"""For study of Cormen's (2001) cut-rods memoization problem, Sec. 15.1."""

def cut_rod(prices, total_segments = None):
    # Bottom-up version
    if total_segments == None:
        total_segments = len(prices)
    revenues = [None for i in range(total_segments + 1)]
    revenues[0] = 0
    for segments in range(total_segments):
        dummy = -max(prices)
        for i in range(1, segments):
            dummy = max(dummy, prices[i] + revenues[segments-i])
        revenues[segments] = dummy
    return revenues[total_segments]
