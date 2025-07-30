
import sys
from collections import *
import copy
import math
import heapq
import queue
input = sys.stdin.readline

# (0 )(1  )  )(())
# def lc1021():
#     s = input()
#     st = []
#     ans = ''
#     for c in s:
#         if c == '(':
#             st.append(c)
#             if len(st) > 1:
#                 ans += c
#         else:
#             st.pop()
#             if st:
#                 ans += c
#     print(ans)


# 请在此输入您的代码
a, b, c = map(int, input().split())
def check(a, b, c):
  if a > (b + c):
    return 'l'
  if b > (a + c):
    return 'q'
  if c > (a + b):
    return 'b'
  return -1

print(check(a, b, c))





# def ksmall():
#     arr = list(map(int, input().split()))
#     k = int(input())
#     heap = [-x for x in arr[:k]]
#     heapq.heapify(heap)
    
#     for x in arr[k:]:
#         if -x > heap[0]:
#             heapq.heappop(heap)
#             heapq.heappush(heap, -x)
#     print(*sorted([-x for x in heap]))




# def _760():
#     n = int(input())
#     ans = [0]

#     "di gui"
#     def calc(n):
#         if n == 0:
#             return
#         n //= 2
#         ans[0] += 1
#         for x in range(1, n+1):
#             calc(x)
#         return ans[0]
#     print(calc(n))    



# a, b, c = map(int, input().split())
# for x in range(1, n + 1):
#   if x % a and x % b and x % c:
#     ans += 1
# def _153():

#     def check(x: int) -> bool:
#         while x:
#             digit = x % 10
#             if digit == 2:
#                 return False
#             x //= 10
#         return True




#     n = int(input())
#     ans = 0
#     for x in range(1, n+1):
#         if check(x):
#             ans += 1

#     print(ans)



# def _549() -> int:
#     n, m = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     ans = [[0] * m for _ in range(n)]
#     d = [(-1, -1), (-1, 0), (-1, 1),
#         (0, -1),            (0, 1),
#          (1, -1),  (1, 0),  (1, 1)]


#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == 1:
#                 ans[i][j] = 9
#             else:
#                 for dx, dy in d:
#                     ii, jj = i + dx, j + dy
#                     if ii < 0 or jj < 0 or ii >= n or jj >= m:
#                         continue
#                     ans[i][j] += arr[ii][jj]
#     for i in range(n):
#         print(*ans[i])
        


# def _143():
#     n = int(input())
#     ans = n
#     while n > 3:
#         n -= 2
#         ans += 1
#     print(ans)
        


# def _550():
#     dire = [(-1, -1), (-1, 0), (-1, 1),
#             (0, -1),           (0, 1),
#             (1, -1),  (1, 0),  (1, 1)]
#     n, m = map(int, input().split())
#     nums = [list(map(int, input().split())) for _ in range(n)]
#     ans = copy.deepcopy(nums)


#     for i in range(n):
#         for j in range(m):
#             cur_sum = 1
#             for dx, dy in dire:
#                 ii = i + dx
#                 jj = j + dy
#                 if ii < 0 or jj < 0 or ii == n or jj == m:
#                     continue
#                 cur_sum += 1
#                 ans[i][j] += nums[ii][jj]

#             ans[i][j] //= cur_sum

#     for i in range(n):
#         print(*ans[i])


# def _156():
#     n, m = map(int, input().split())
#     i, j = map(int, input().split())
#     nums = [[0] * m for _ in range(n)]   #create a matrix
#     i -= 1
#     j -= 1
#     x, y = 0, 0
#     cur = nums[0][0] = 1
    

#     while cur < n * m:
#         #turn right first
#         while y+1 < m and nums[x][y+1] == 0:
            
#             cur += 1
#             y += 1
#             nums[x][y] = cur
        
        
#         #then turn down
#         while x+1 < n and nums[x+1][y] == 0:
            
#             cur += 1
#             x += 1
#             nums[x][y] = cur

#         #turn left
#         while y-1 > -1 and nums[x][y-1] == 0:
            
#             cur += 1
#             y -= 1
#             nums[x][y] = cur
        

#         #toward up
#         while x-1 > -1 and nums[x-1][y] == 0:
            
#             cur += 1
#             x -= 1
#             nums[x][y] = cur
        
    
#     print(nums[i][j])

# def B():
#     def che(n):
#         jc = math.factorial(n)
#         sm = n * (n + 1) // 2
#         return ((sm - jc) % 100) == 0
#     # n = int(input())
#     ans = 0
#     for x in range(1, 2024041331404203):
#         if che(x):
#             ans += 1
#     print(ans)


# def hnt():
#     n, m = map(int, input().split())
#     ans = [0]
#     def move(n, A, B, C):
        
#         if n == 0: 
#             return
        
        
#         move(n-1, A, C, B)
#         ans[0] += 1
#         if ans[0] == m:
#             print(f"#{m}: {A}->{C}")
#             return
        
#         move(n-1, B, A, C)
    
    
#     move(n, 'A', 'B', 'C')
#     print(2 ** n - 1)


