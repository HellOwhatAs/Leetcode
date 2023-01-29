#
# @lc app=leetcode.cn id=2373 lang=python3
#
# [2373] 矩阵中的局部最大值
#

# @lc code=start
from typing import List
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                maxLocal[i][j] = max(
                    max(grid[i][j:j+3]), 
                    max(grid[i+1][j:j+3]), 
                    max(grid[i+2][j:j+3])
                )
        return maxLocal
# @lc code=end

print(Solution().largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]))