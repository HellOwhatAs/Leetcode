#
# @lc app=leetcode.cn id=2367 lang=python3
#
# [2367] 算术三元组的数目
#

# @lc code=start
from typing import List
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        idx, ret = set(nums), 0
        for i in range(diff, 201 - diff):
            if i in idx and (i - diff) in idx and (i + diff) in idx:
                ret += 1
        return ret
# @lc code=end

