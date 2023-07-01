#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dp = {}
        for idx, elem in enumerate(nums):
            if elem in dp: return [dp[elem], idx]
            dp[target - elem] = idx
# @lc code=end

print(Solution().twoSum(nums = [2,7,11,15], target = 9))
print(Solution().twoSum(nums = [3,2,4], target = 6))
print(Solution().twoSum(nums = [3,3], target = 6))