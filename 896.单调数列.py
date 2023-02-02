#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#

# @lc code=start
from typing import List
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return all(nums[i - 1] >= nums[i] for i in range(1, len(nums))) or all(nums[i - 1] <= nums[i] for i in range(1, len(nums)))
# @lc code=end

