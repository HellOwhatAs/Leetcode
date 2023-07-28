#
# @lc app=leetcode.cn id=1260 lang=python3
#
# [1260] 二维网格迁移
#

# @lc code=start
from typing import List
import numpy as np
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        grid: np.ndarray = np.array(grid)
        for _ in range(k):
            grid[:, 1:], grid[:, 0] = grid[:, :-1], grid[:, -1].copy()
            grid[1:, 0], grid[0, 0] = grid[:-1, 0], grid[-1, 0].copy()
        return grid.tolist()
# @lc code=end

print(Solution().shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1))
print(Solution().shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))
print(Solution().shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9))