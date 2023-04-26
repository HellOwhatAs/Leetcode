#
# @lc app=leetcode.cn id=1031 lang=python3
#
# [1031] 两个非重叠子数组的最大和
#

# @lc code=start
from typing import List
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        return max(self.func(nums, firstLen, secondLen), self.func(nums, secondLen, firstLen))
    def func(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        maxSumL = suml = sum(nums[:firstLen])
        sumr = sum(nums[firstLen: firstLen + secondLen])
        res = maxSumL + sumr
        for i in range(firstLen + secondLen, len(nums)):
            j = i - secondLen
            suml += nums[j] - nums[j - firstLen]
            maxSumL = max(maxSumL, suml)
            sumr += nums[i] - nums[i - secondLen]
            res = max(res, maxSumL + sumr)
        return res
# @lc code=end

print(Solution().maxSumTwoNoOverlap(nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2))