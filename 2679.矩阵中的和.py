#
# @lc app=leetcode.cn id=2679 lang=python3
#
# [2679] 矩阵中的和
#

# @lc code=start
from typing import List
import numpy as np
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        mat = np.array(nums, dtype=np.int32)
        mat.sort(1)
        return int(mat.max(0).sum())

# @lc code=end

print(Solution().matrixSum(nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]))
print(Solution().matrixSum(nums = [[1]]))