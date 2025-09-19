if True:
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
    inf = float("inf")


import os
import sys

# 请在此输入您的代码
s = input()
ans = []
for c in s:
  if ord(c) in range(48, 58):
    ans.append('Q')
  else:
    ans.append('L')
print(*ans)



# def sol():
#     n = int(input())
#     nums = list(map(int, input().split()))
#     nums.sort()
#     nums1 = [x for x in nums if not(x & 1)]
#     nums2 = [x for x in nums if (x & 1)]
#     nums = (nums1 + nums2)
#     print(*nums)



# """ababbcccc"""
# t = int(input())
# def check():
#     s = input().strip()
#     st = []
#     for c in s:
#         if c not in st:
#             st.append(c)
#             if ord(c) - ord(st[-1]) > 1:
#                 return 'No'
#     return 'Yes'
# for x in range(t):
#     n = int(input())
#     print(check())



# def lq364():
#     l, n, m = mii()
#     left, right = 1, l
#     arr = []
#     ans = -1
#     for _ in range(n):
#         arr.append(ii())
#     arr.append(l)

#     def ok(x):
#         last = cnt = 0
#         for idx in range(n + 1):
#             if arr[idx] - last >= x:
#                 last = arr[idx]
#             else:
#                 cnt += 1
#         return cnt <= m


#     while left <= right:
#         mid = left + (right - left) // 2
#         if ok(mid):
#             left = mid + 1
#             ans = mid
#         else:
#             right = mid - 1
#     print(ans)



    
# def lq99():
#     n, k = mii()
#     lis = []
#     ans = 1

#     for _ in range(n):
#         lis.append(lmi())


#     l, r = 1, 100000
#     while l <= r:
#         mid = l + (r - l) // 2
#         cnt = 0
#         for x, y in lis:
#             cnt += (x // mid) * (y // mid)
#             if cnt >= k:
#                 break
#         if cnt >= k:
#             ans = mid
#             l = mid + 1
#         else:
#             r = mid - 1
#     print(ans)

            
        




# t = ii()
# def check(n, k):
#     print("Blueberry" if n % (k+1) != 0 else "Strawberry")


# for _ in range(t):
#     n, k = mii()
#     check(n, k)




# def solve():
#     nums = [1,2,3,4]
#     n = len(nums)
#     k = 2
#     if n % k:
#         print('False')
#     else:
#         g = n // k
#         for f in Counter(nums).values():
#             if f > g:
#                 print('False')

#         print('True')

# def maximumSubarraySum(nums: list[int], k: int) -> int:
#     n = len(nums)
#     ans = 0
#     win = []
#     l = cur = 0
#     for r in range(n):
#         cur += nums[r]
#         win.append(nums[r])
#         if r - l < k - 1:
#             continue
#         elif len(set(win)) < k:
#             cur -= nums[l]
#             win.pop(0)
#             l += 1

#         else:
#             ans = max(ans, cur)
#             cur -= nums[l]
#             win.pop()
#             l += 1

#     return ans


# def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
#     if not(k):
#         return 0
#     l = ans = 0
#     cur = 1
#     n = len(nums)
#     for r, x in enumerate(nums):
#         cur *= x

#         while l < n and cur >= k:
#             cur //= nums[l]
#             l += 1

#         ans += (r - l + 1)
#     return ans if ans > 0 else 0



# def maximumLengthSubstring(s: str) -> int:
#     l = ans = 0
#     st = defaultdict(int)
#     for r, c in enumerate(s):
#         st[c] += 1
#         while st[c] > 2:
#             st[s[l]] -= 1
#             l += 1
#         ans = max(ans, r - l + 1)
#     return ans



