if 1:
    import sys
    input = sys.stdin.readline
    import math
    from itertools import *
    from collections import *
    from bisect import *
    import heapq
    import random
    
    # import numpy as np





def lq209():
    s1 = list(input().strip())
    s2 = list(input().strip()) # target
    n = len(s1)
    ans = 0
    for i in range(n-1):
        if s1[i] != s2[i]:
            ans += 1
            s1[i] = '*' if s1[i] == 'o' else 'o'
            s1[i+1] = '*' if s1[i+1] == 'o' else 'o'
    print(ans)

lq209()




# dic = defaultdict(int)
# for _ in range(100000):
#     x = random.randint(0, 9)
#     dic[x] += 1

# dic = sorted(dic.items(), key=lambda x: x[1])
# print(dic)


# def lq532():
#     mx = int(input())
#     n = int(input())
#     nums = []
#     ans = 0
#     for _ in range(n):
#         nums.append(int(input()))
    
#     nums.sort()
#     l, r = 0, n-1
#     while l <= r:
#         if nums[l] + nums[r] <= mx:
#             l += 1
#             r -= 1
#         else:
#             r -= 1
#         ans += 1
#     print(ans)







# def lq545():
#     n = int(input())
#     nums = list(map(int, input().split()))
#     # nums.sort()
#     ans = 0
#     # for i in range(1, n):
#     #     nums[i] += nums[i-1]
#     # print(sum(nums[1:]))
#     heapq.heapify(nums)
#     while len(nums) > 1:
#         x = heapq.heappop(nums)
#         y = heapq.heappop(nums)
#         ans += x + y
#         heapq.heappush(nums, x + y)
#     print(ans)



# def lq3291():
#     while 1:
#         try:
#             n, m = map(int, input().split())
#             nums = list(map(int, input().split()))
#             n = len(nums)
#             diff = [0] * n
#             diff[0] = nums[0]
#             for i in range(1, n):
#                 diff[i] = nums[i] - nums[i-1]

#             for _ in range(m):
#                 x, y, z = map(int, input().split())
#                 diff[x-1] += z
#                 if y < n:
#                     diff[y] -= z


#             print(*list(accumulate(diff)))
        
#         except:
#             break
#2D diff arr

# def twoDdiff():
#     n, m = map(int, input().split())
#     matrix = [list(map(int, input().split())) for _ in range(n)]
#     print(np.array(matrix))
#     print("-----------------------")
#     def prefix(matrix):
#         pre_sum = [[0] * (m+1) for _ in range(n+1)]
#         for i in range(1, n+1):
#             for j in range(1, m+1):
#                 pre_sum[i][j] = pre_sum[i-1][j] + pre_sum[i][j-1] - pre_sum[i-1][j-1] + matrix[i-1][j-1]
#         return pre_sum
    

#     def diff(matrix):
#         diffnums = [[0] * m for _ in range(n)]
#         for i in range(n):
#             for j in range(m):
#                 diffnums[i][j] = matrix[i][j] - (matrix[i-1][j] if i > 0 else 0) - (matrix[i][j-1] if j > 0 else 0) + (matrix[i-1][j-1] if i > 0 and j > 0 else 0)
#         return diffnums
    
#     print(np.array(prefix(matrix)))
#     print("-----------------------")
#     print(np.array(diff(matrix)))

# twoDdiff()
# print(list(accumulate([1, 2, 3, 4])))


