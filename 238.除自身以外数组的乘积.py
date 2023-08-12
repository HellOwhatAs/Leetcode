#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
from typing import List
from math import log, exp

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        offset = -1 if sum(1 for _ in nums if _ < 0) & 1 else 1
        total = sum(log(abs(x)) for x in nums if x != 0)
        if nums.count(0) > 1: return [0] * len(nums)
        if nums.count(0) == 1:
            zero_idx = nums.index(0)
            return [offset * round(exp(total)) if i == zero_idx else 0 for i in range(len(nums))]
        return [round(exp(total - log(abs(i)))) * offset * (-1 if i < 0 else 1) for i in nums]
# @lc code=end

print(Solution().productExceptSelf(nums = [1,2,3,4]))
print(Solution().productExceptSelf([-1,1,0,-3,3]))
print(Solution().productExceptSelf([9,0,-2]))