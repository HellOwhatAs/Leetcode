#
# @lc app=leetcode.cn id=2529 lang=python3
#
# [2529] 正整数和负整数的最大计数
#

# @lc code=start
from typing import List
from bisect import bisect_left, bisect_right
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(bisect_left(nums, 0), len(nums) - bisect_right(nums, 0))
# @lc code=end

print(Solution().maximumCount([-2,-1,-1,1,2,3]))
print(Solution().maximumCount([-3,-2,-1,0,0,1,2]))
print(Solution().maximumCount([5,20,66,1314]))