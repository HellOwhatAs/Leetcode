#
# @lc app=leetcode.cn id=1909 lang=python3
#
# [1909] 删除一个元素使数组严格递增
#

# @lc code=start
from typing import List
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n, top, count = len(nums), -1, 0
        for i in range(n):
            if (nums[i] > top):
                top = nums[i]
            elif ((i > 1 and nums[i] > nums[i - 2]) or (i < 2)):
                count += 1
                top = nums[i]
            else:
                count += 1
        return count <= 1 
# @lc code=end

print(Solution().canBeIncreasing([100, 21, 100]))