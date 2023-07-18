#
# @lc app=leetcode.cn id=2731 lang=python3
#
# [2731] 移动机器人
#

# @lc code=start
from typing import List
class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        n, MOD = len(nums), 10**9+7
        nums = sorted([nums[i] + (d if s[i] == 'R' else -d) for i in range(n)])
        ret = 0
        for i in range(1, n):
            ret += (nums[i] - nums[i-1]) % MOD * i % MOD * (n-i)
            ret %= MOD
        return ret
# @lc code=end

