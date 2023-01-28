#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret=0
        for i in nums:
            ret^=i
        return ret
# @lc code=end
