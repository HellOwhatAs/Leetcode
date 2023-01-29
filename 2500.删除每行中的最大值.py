#
# @lc app=leetcode.cn id=2500 lang=python3
#
# [2500] 删除每行中的最大值
#

# @lc code=start
from typing import List
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m, n, ret = len(grid), len(grid[0]), 0
        for row in grid: row.sort()
        for i in range(n):
            ret += max(grid[j][i] for j in range(m))
        return ret
# @lc code=end

