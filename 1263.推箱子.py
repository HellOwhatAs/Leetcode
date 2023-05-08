#
# @lc app=leetcode.cn id=1263 lang=python3
#
# [1263] 推箱子
#

# @lc code=start
from typing import List
from collections import deque
from math import inf
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        sx, sy, bx, by = None, None, None, None
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 'S':
                    sx, sy = x, y
                elif grid[x][y] == 'B':
                    bx, by = x, y

        ok = lambda x, y: (0 <= x < m and 0 <= y < n and grid[x][y] != '#')
        d = [0, -1, 0, 1, 0]
        dp = [[inf] * (m * n) for _ in range(m * n)]
        dp[sx * n + sy][bx * n + by] = 0
        q = deque([(sx * n + sy, bx * n + by)])
        while q:
            q1 = deque()
            while q:
                s1, b1 = q.popleft()
                sx1, sy1 = s1 // n, s1 % n
                bx1, by1 = b1 // n, b1 % n
                if grid[bx1][by1] == 'T':
                    return dp[s1][b1]
                for i in range(4):
                    sx2, sy2 = sx1 + d[i], sy1 + d[i + 1]
                    s2 = sx2 * n + sy2
                    if not ok(sx2, sy2):
                        continue
                    if sx2 == bx1 and sy2 == by1:
                        bx2, by2 = bx1 + d[i], by1 + d[i + 1]
                        b2 = bx2 * n + by2
                        if not ok(bx2, by2) or dp[s2][b2] <= dp[s1][b1] + 1:
                            continue
                        dp[s2][b2] = dp[s1][b1] + 1
                        q1.append((s2, b2))
                    else:
                        if dp[s2][b1] <= dp[s1][b1]:
                            continue
                        dp[s2][b1] = dp[s1][b1]
                        q.append((s2, b1))
            q, q1 = q1, q
        return -1
# @lc code=end

