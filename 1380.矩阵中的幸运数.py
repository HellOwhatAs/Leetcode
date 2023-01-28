#
# @lc app=leetcode.cn id=1380 lang=python3
#
# [1380] 矩阵中的幸运数
#

# @lc code=start
from typing import List
import numpy as np
from itertools import product
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        mat = np.array(matrix, dtype=np.int32)
        m, n = mat.shape
        ret = []
        for i, j in product(range(m), range(n)):
            if mat[i, j] == np.min(mat[i]) == np.max(mat[:, j]):
                ret.append(int(mat[i, j]))
        return ret
# @lc code=end

