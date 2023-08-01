#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while j < len(nums):
            if nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
# @lc code=end
nums = [0, 1]
Solution().moveZeroes(nums)
print(nums)