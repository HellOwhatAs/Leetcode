#
# @lc app=leetcode.cn id=892 lang=python3
#
# [892] 三维形体的表面积
#

# @lc code=start
from typing import List
import numpy as np
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        ret = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0: ret += 2
                if j != 0: ret += abs(grid[i][j] - grid[i][j-1]) + abs(grid[j][i] - grid[j-1][i])
            ret += grid[i][0] + grid[i][-1] + grid[0][i] + grid[-1][i]
        return ret
# @lc code=end

