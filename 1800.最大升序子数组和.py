#
# @lc app=leetcode.cn id=1800 lang=python3
#
# [1800] 最大升序子数组和
#

# @lc code=start
from typing import List
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        breaks=[i for i in range(1,len(nums)) if nums[i-1]>=nums[i]]
        return max(sum(nums[breaks[i] if i>-1 else None:breaks[i+1] if i+1<len(breaks) else None]) for i in range(-1,len(breaks)))
# @lc code=end

print(Solution().maxAscendingSum([10,20,30,5,10,50]))