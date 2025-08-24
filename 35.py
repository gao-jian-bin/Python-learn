if 1:
    import sys
    from math import *
    from itertools import *
    from collections import *
    from bisect import *
    from heapq import *
    input = lambda: sys.stdin.readline().rstrip()
    ii = lambda: int(input())
    mii = lambda: map(int, input().split())
    lmi = lambda: list(map(int, input().split()))


def solve():
    nums = [1,2,3,4]
    n = len(nums)
    k = 2
    if n % k:
        print('False')
    else:
        g = n // k
        for f in Counter(nums).values():
            if f > g:
                print('False')

        print('True')


solve()