#
# @lc app=leetcode.cn id=2395 lang=python3
#
# [2395] 和相等的子数组
#

# @lc code=start
from typing import List
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums = set()
        for i in range(1, len(nums)):
            tmp = nums[i - 1] + nums[i]
            if tmp in sums: return True
            sums.add(tmp)
        return False
# @lc code=end

