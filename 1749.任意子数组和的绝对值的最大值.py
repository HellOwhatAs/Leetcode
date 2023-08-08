#
# @lc app=leetcode.cn id=1749 lang=python3
#
# [1749] 任意子数组和的绝对值的最大值
#

# @lc code=start
from typing import List
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max, dp_min = [None] * n, [None] * n
        dp_max[0] = dp_min[0] = nums[0]
        for i in range(1, n):
            dp_max[i] = max(nums[i], dp_max[i-1] + nums[i])
            dp_min[i] = min(nums[i], dp_min[i-1] + nums[i])
        return max(max(dp_max), -min(dp_min))
# @lc code=end

print(Solution().maxAbsoluteSum(nums = [1,-3,2,3,-4]))
print(Solution().maxAbsoluteSum(nums = [2,-5,1,-4,3,-2]))