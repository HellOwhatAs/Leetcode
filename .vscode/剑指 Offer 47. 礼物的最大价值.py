from typing import List
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def dp(self, x: int, y: int) -> int:
        if x == self.m - 1 and y == self.n - 1: return self.grid[x][y]
        if x == self.m - 1: return self.grid[x][y] + self.dp(x, y + 1)
        if y == self.n - 1: return self.grid[x][y] + self.dp(x + 1, y)
        return self.grid[x][y] + max(self.dp(x + 1, y), self.dp(x, y + 1))
    def maxValue(self, grid: List[List[int]]) -> int:
        self.grid, self.m, self.n = grid, len(grid), len(grid[0])
        return self.dp(0, 0)

print(Solution().maxValue([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))