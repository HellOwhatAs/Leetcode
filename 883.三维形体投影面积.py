#
# @lc app=leetcode.cn id=883 lang=python3
#
# [883] 三维形体投影面积
#

# @lc code=start
from typing import List
import numpy as np
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        grid2 = np.array(grid, dtype=np.int32)
        return int(np.sum(grid2 != 0) + np.sum(np.max(grid2, axis=0)) + np.sum(np.max(grid2, axis=1)))
# @lc code=end

print(Solution().projectionArea([[1,0],[0,2]]))