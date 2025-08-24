if 1:
    import sys
    from math import *
    from itertools import *
    from collections import *
    from bisect import *
    import heapq
    input = lambda: sys.stdin.readline().rstrip()
    ii = lambda: int(input())
    mii = lambda: map(int, input().split())
    lmi = lambda: list(map(int, input().split()))



m = input()
print(m)
n = input()
print(n)
# def lq1621():
#     n, m, k = mii()   #nums 至少有 k 个数要大于等于 m
#     nums = lmi
#     ans = cur = 0
#     l = r = 0
#     while l < n:
#         while r < n and cur < k:
#             if nums[r] >= m:
#                 cur += 1
#             r += 1
#         if cur == k:
#             ans += n - r + 1
#         if nums[l] >= m:
#             cur -= 1
#         l += 1

#     print(ans)





# def lq1372():
#     n, s = map(int, input().split())
#     nums = list(map(int, input().split()))
#     l = cur = 0
#     ans = n
#     for r in range(n):
#         cur += nums[r]
#         while cur >= s:
#             ans = min(ans, r - l + 1)
#             cur -= nums[l]
#             l += 1

#     print(0 if ans == n else ans)
            
        

# def lq1371():
#     ss = input().strip()
#     def f(ss):
#         n = len(ss)
#         mid = n // 2
#         for i in range(mid):
#             if ss[i] != ss[n - i -1]:
#                 return 'N'
#         return 'Y'



#     print(f(ss))

# lq1371()




# def lq532():
#     mx = int(input())
#     n = int(input())
#     arr = []
#     ans = 0
#     for _ in range(n):
#         arr.append(int(input()))
    
#     arr.sort()
#     l, r = 0, n - 1
#     while l <= r:
#         if arr[l] + arr[r] <= mx:
#             ans += 1
#             l += 1
#             r -= 1
#         else:
#             ans += 1
#             r -= 1

#     print(ans)

