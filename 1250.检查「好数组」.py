#
# @lc app=leetcode.cn id=1250 lang=python3
#
# [1250] 检查「好数组」
#

# @lc code=start
from typing import List
from math import gcd
from functools import reduce
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return reduce(gcd, nums) == 1
# @lc code=end

