#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心下标
#

# @lc code=start
from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum, rightsum = 0, sum(nums[1:])
        if leftsum == rightsum: return 0
        for ret in range(1, len(nums)):
            leftsum += nums[ret - 1]
            rightsum -= nums[ret]
            if leftsum == rightsum: return ret
        return -1
# @lc code=end

print(Solution().pivotIndex([2, 1, -1]))