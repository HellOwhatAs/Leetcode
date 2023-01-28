#
# @lc app=leetcode.cn id=598 lang=python3
#
# [598] 范围求和 II
#

# @lc code=start
from typing import List
import numpy as np
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for x, y in ops: m, n = min(m, x), min(n, y)
        return m*n
# @lc code=end

print(Solution().maxCount(m = 3, n = 3, ops = []))