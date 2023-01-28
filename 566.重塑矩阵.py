#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
from typing import List
import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        try:
            return np.array(mat, dtype=np.int32).reshape((r, c)).tolist()
        except:
            return mat
# @lc code=end

