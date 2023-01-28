#
# @lc app=leetcode.cn id=1582 lang=python3
#
# [1582] 二进制矩阵中的特殊位置
#

# @lc code=start
from typing import List
import numpy as np
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, ret = np.array(mat, dtype=np.int32), 0
        for i in range(m.shape[0]):
            for j in range(m.shape[1]):
                if m[i,j] and np.sum(m[i,:])==1 and np.sum(m[:,j])==1:
                    ret+=1
        return ret
# @lc code=end

