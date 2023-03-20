from typing import List
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in reversed(range(m - 1)):
            grid[i][n - 1] += grid[i + 1][n - 1]
        for j in reversed(range(n - 1)):
            grid[m - 1][j] += grid[m - 1][j + 1]
        for i in reversed(range(m - 1)):
            for j in reversed(range(n - 1)):
                grid[i][j] += max(grid[i + 1][j], grid[i][j + 1])
        return grid[0][0]

print(Solution().maxValue([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))