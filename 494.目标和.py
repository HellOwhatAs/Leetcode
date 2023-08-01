#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
from typing import List
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def dfs(self, start: int, val: int):
        if start == len(self.nums): return val == self.targrt
        return self.dfs(start + 1, val + self.nums[start]) + self.dfs(start + 1, val - self.nums[start])

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums, self.targrt = nums, target
        return self.dfs(0, 0)
# @lc code=end

print(Solution().findTargetSumWays(nums = [1,1,1,1,1], target = 3))
print(Solution().findTargetSumWays(nums = [1], target = 1))
print(Solution().findTargetSumWays([50,37,6,20,35,41,45,3,20,36,49,1,20,10,43,4,44,15,44,34], 25))