#
# @lc app=leetcode.cn id=2133 lang=python3
#
# [2133] 检查是否每一行每一列都包含全部整数
#

# @lc code=start
from typing import List
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        standard = set(range(1, n+1))
        for i in range(n):
            if set(matrix[i]) != standard or set(matrix[j][i] for j in range(n)) != standard: return False
        return True
# @lc code=end

print(Solution().checkValid([[1,1,1],[1,2,3],[1,2,3]]))