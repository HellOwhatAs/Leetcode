#
# @lc app=leetcode.cn id=1413 lang=python3
#
# [1413] 逐步求和得到正数的最小值
#

# @lc code=start
from typing import List
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        val, ret = 0, float('inf')
        for i in nums:
            val += i
            ret = min(ret, val)
        return max(1, 1 - ret)
# @lc code=end

