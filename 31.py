
import sys
from collections import *
input = sys.stdin.readline



# a, b, c = map(int, input().split())
# for x in range(1, n + 1):
#   if x % a and x % b and x % c:
#     ans += 1
def _153():

    def check(x: int) -> bool:
        while x:
            digit = x % 10
            if digit == 2:
                return False
            x //= 10
        return True




    n = int(input())
    ans = 0
    for x in range(1, n+1):
        if check(x):
            ans += 1

    print(ans)



def _549() -> int:
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = [[0] * m for _ in range(n)]
    d = [(-1, -1), (-1, 0), (-1, 1),
        (0, -1),            (0, 1),
         (1, -1),  (1, 0),  (1, 1)]


    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                ans[i][j] = 9
            else:
                for dx, dy in d:
                    ii, jj = i + dx, j + dy
                    if ii < 0 or jj < 0 or ii >= n or jj >= m:
                        continue
                    ans[i][j] += arr[ii][jj]
    print()
    print()
    for i in range(n):
        print(*ans[i])
        


_549()

