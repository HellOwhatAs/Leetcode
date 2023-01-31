#
# @lc app=leetcode.cn id=1512 lang=python3
#
# [1512] 好数对的数目
#

# @lc code=start
from typing import List
from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(v * (v - 1) // 2 for v in Counter(nums).values())
# @lc code=end

