#
# @lc app=leetcode.cn id=1139 lang=python3
#
# [1139] 最大的以 1 为边界的正方形
#

# @lc code=start
from typing import List, Tuple
from itertools import product
class Solution:
    def test(self, a: Tuple[int, int], b: Tuple[int, int]) -> bool:
        (x1, y1), (x2, y2) = a, b
        if x1 == x2: return self.left[x1][y2] >= y2 - y1 + 1
        return self.up[x2][y1] >= x2 - x1 + 1
    def build(self) -> None:
        self.up = [[0] * self.n for _ in range(self.m)]
        for i in range(self.n): self.up[0][i] = self.grid[0][i]
        for i, j in product(range(1, self.m), range(self.n)): self.up[i][j] = self.up[i - 1][j] + 1 if self.grid[i][j] else 0
        self.left = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m): self.left[i][0] = self.grid[i][0]
        for i, j in product(range(1, self.n), range(self.m)): self.left[j][i] = self.left[j][i - 1] + 1 if self.grid[j][i] else 0
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.m, self.n = m, n
        self.grid = grid
        ret = 0
        self.build()
        for x1, y1 in product(range(m), range(n)):
            for x2 in range(x1, m):
                y2 = y1 + x2 - x1
                if y2 >= n: continue
                if all((
                    self.test((x1, y1), (x1, y2)),
                    self.test((x2, y1), (x2, y2)),
                    self.test((x1, y1), (x2, y1)),
                    self.test((x1, y2), (x2, y2))
                )): ret = max(ret, (x2 - x1 + 1) * (y2 - y1 + 1))
        return ret

                
# @lc code=end

print(Solution().largest1BorderedSquare(grid = [[1,1,1],[1,0,1],[1,1,1]]))
print(Solution().largest1BorderedSquare(grid = [[1,1,0,0]]))

print(Solution().largest1BorderedSquare([
 [1,1,1],
 [1,1,0],
 [1,1,1],
 [0,1,1],
 [1,1,1]]))