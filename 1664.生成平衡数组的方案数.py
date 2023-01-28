#
# @lc app=leetcode.cn id=1664 lang=python3
#
# [1664] 生成平衡数组的方案数
#

# @lc code=start
from typing import List
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        summer, summer1 = [0] * len(nums), [0] * len(nums)
        summer[-2], summer[-1] = nums[-2], nums[-1]
        summer1[0], summer1[1] = nums[0], nums[1]
        for i in range(len(nums)-3, -1, -1):
            summer[i] = summer[i + 2] + nums[i]
        for i in range(2, len(nums)):
            summer1[i] = summer1[i - 2] + nums[i]
        ret = 0
        for i in range(len(nums)):
            rightsum = summer[i+1:min(i+3, len(nums))]
            leftsum = summer1[max(0, i-2):i]
            if len(rightsum)<2: rightsum.extend([0]*(2-len(rightsum)))
            if len(leftsum)<2 : leftsum = [0]*(2-len(leftsum)) + leftsum
            if leftsum[0] + rightsum[0] == leftsum[1] + rightsum[1]:
                ret += 1
        return ret
# @lc code=end

print(Solution().waysToMakeFair([1]))