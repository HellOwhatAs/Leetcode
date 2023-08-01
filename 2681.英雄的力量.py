#
# @lc app=leetcode.cn id=2681 lang=python3
#
# [2681] 英雄的力量
#

# @lc code=start
from typing import List
class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()
        dp, pre_sum, res, mod = 0, 0, 0, 10**9 + 7
        for i in range(len(nums)):
            dp = (pre_sum + nums[i]) % mod
            pre_sum = (pre_sum + dp) % mod
            res = (res + dp * nums[i] ** 2) % mod
        return res

# @lc code=end

print(Solution().sumOfPower(nums = [2,1,4]))