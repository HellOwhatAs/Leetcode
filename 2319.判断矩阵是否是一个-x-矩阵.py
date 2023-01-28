#
# @lc app=leetcode.cn id=2319 lang=python3
#
# [2319] 判断矩阵是否是一个 X 矩阵
#

# @lc code=start
from typing import List
from itertools import product
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i, j in product(range(n), range(n)):
            if i == j or i + j == n - 1:
                if grid[i][j] == 0: return False
            else:
                if grid[i][j] != 0: return False
        return True
# @lc code=end

