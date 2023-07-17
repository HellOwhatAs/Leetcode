#
# @lc app=leetcode.cn id=1685 lang=python3
#
# [1685] 有序数组中差绝对值之和
#

# @lc code=start
from typing import List
class Solution:
    
    def func(self, nums: List[int]) -> List[int]:
        ret = [0]
        for i in range(1, len(nums)):
            ret.append(ret[-1] + abs(nums[i] - nums[i-1]) * i)
        return ret
    
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left = self.func(nums)
        nums.reverse()
        right = self.func(nums)
        right.reverse()
        return [l+r for l, r in zip(left, right)]
# @lc code=end

print(Solution().getSumAbsoluteDifferences(nums = [2,3,5]))