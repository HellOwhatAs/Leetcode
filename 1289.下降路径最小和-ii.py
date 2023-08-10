#
# @lc app=leetcode.cn id=1289 lang=python3
#
# [1289] 下降路径最小和  II
#

# @lc code=start
from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[None] * n for _ in range(n)]
        dp[0] = grid[0]
        for i in range(1, n):
            for j in range(n):
                dp[i][j] = min(dp[i-1][k] for k in range(n) if k != j) + grid[i][j]
        return min(dp[-1])
# @lc code=end

print(Solution().minFallingPathSum(grid = [[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().minFallingPathSum(grid = [[7]]))