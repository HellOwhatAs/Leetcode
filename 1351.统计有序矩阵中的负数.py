#
# @lc app=leetcode.cn id=1351 lang=python3
#
# [1351] 统计有序矩阵中的负数
#

# @lc code=start
from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n, ret = len(grid), len(grid[0]), 0
        for i in range(n):
            if grid[0][i] < 0:
                ret += n - i
                break
        else:
            for i in range(m):
                if grid[i][-1] < 0:
                    break
            else: return 0
            
            row, i = i, n - 1
            while row < m:
                while i>=0 and grid[row][i] < 0:
                    i -= 1
                i += 1
                ret += n - i
                row += 1

            return ret

        row = 1
        while row < m:
            while i >= 0 and grid[row][i] < 0:
                i -= 1
            i += 1
            ret += n - i
            row += 1
        return ret
# @lc code=end

print(Solution().countNegatives([[ 4,  3,  2, -1],
                                 [ 3,  2,  1, -1],
                                 [ 1,  1, -1, -2],
                                 [-1, -1, -2, -3]]))

print(Solution().countNegatives([[3, 2],
                                 [1, 0]]))