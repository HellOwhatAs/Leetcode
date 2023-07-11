#
# @lc app=leetcode.cn id=1911 lang=python3
#
# [1911] 最大子序列交替和
#

# @lc code=start
from typing import List
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(nums))]
        dp[0] = [nums[0], 0]
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + nums[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - nums[i])
        return dp[-1][0]
# @lc code=end

print(Solution().maxAlternatingSum(nums = [4,2,5,3]))
print(Solution().maxAlternatingSum(nums = [5,6,7,8]))
print(Solution().maxAlternatingSum(nums = [6,2,1,2,4,5]))