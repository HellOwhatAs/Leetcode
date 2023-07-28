#
# @lc app=leetcode.cn id=2760 lang=python3
#
# [2760] 最长奇偶子数组
#

# @lc code=start
from typing import List
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        dp = [None] * len(nums)
        dp[0] = 0 if nums[0] > threshold else 1
        for i in range(1, len(nums)):
            if nums[i] > threshold: dp[i] = 0
            elif nums[i] % 2 == nums[i - 1] % 2: dp[i] = 1
            else: dp[i] = dp[i-1] + 1
        for i in range(len(dp)):
            if dp[i]: dp[i] -= nums[i - dp[i] + 1] % 2
        return max(dp)

# @lc code=end

print(Solution().longestAlternatingSubarray(nums = [3,2,5,4], threshold = 5))
print(Solution().longestAlternatingSubarray(nums = [1,2], threshold = 2))
print(Solution().longestAlternatingSubarray(nums = [2,3,4,5], threshold = 4))
print(Solution().longestAlternatingSubarray([8,4], 6))