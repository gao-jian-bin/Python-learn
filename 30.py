import sys
from collections import *
input = sys.stdin.readline


def P1115():
    n = int(input())
    arr = list(map(int, input().split()))
    cur = arr[0]
    mx = arr[0]
    for i in range(1, n):
        cur = max(arr[i], cur + arr[i])
        mx = max(mx, cur)

    return mx




def P1886():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    max_deque = deque()
    min_deque = deque()
    mi = []
    mx = []
    
    for i in range(n):

        while max_deque and nums[max_deque[-1]] <= nums[i]:
            max_deque.pop()
        max_deque.append(i)
        
        while min_deque and nums[min_deque[-1]] >= nums[i]:
            min_deque.pop()
        min_deque.append(i)

        if max_deque[0] <= i - k:
            max_deque.popleft()
        if min_deque[0] <= i - k:
            min_deque.popleft()
        if i >= k - 1:
            mi.append(nums[min_deque[0]])
            mx.append(nums[max_deque[0]])
    
    print(*mi)
    print(*mx)
"""
8 3
1 3 -1 -3 5 3 6 7

"""

P1886()
