#
# @lc app=leetcode.cn id=1886 lang=python3
#
# [1886] 判断矩阵经轮转后是否一致
#

# @lc code=start
from typing import List
import numpy as np
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        m, t = np.array(mat, dtype=np.bool8), np.array(target, dtype=np.bool8)
        if (m == t).all(): return True
        if ((m:=np.rot90(m, -1)) == t).all(): return True
        if ((m:=np.rot90(m, -1)) == t).all(): return True
        if (np.rot90(m, -1) == t).all(): return True
        return False
# @lc code=end

print(Solution().findRotation(mat = [[0,1],[1,1]], target = [[1,0],[0,1]]))