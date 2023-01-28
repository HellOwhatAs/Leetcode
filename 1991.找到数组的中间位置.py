#
# @lc app=leetcode.cn id=1991 lang=python3
#
# [1991] 找到数组的中间位置
#

# @lc code=start
from typing import List
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        middleIndex, leftsum, rightsum, tmp = 0, 0, sum(nums) - nums[0], len(nums) - 1
        while leftsum != rightsum and middleIndex < tmp:
            leftsum += nums[middleIndex]
            middleIndex += 1
            rightsum -= nums[middleIndex]
        return middleIndex if leftsum == rightsum else -1
# @lc code=end

print(Solution().findMiddleIndex([2,3,-1,8,4]))