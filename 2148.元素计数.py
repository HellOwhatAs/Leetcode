#
# @lc app=leetcode.cn id=2148 lang=python3
#
# [2148] 元素计数
#

# @lc code=start
from typing import List
import bisect
class Solution:
    def countElements(self, nums: List[int]) -> int:
        return nums.sort() or max(0, bisect.bisect_left(nums, nums[-1]) - bisect.bisect_right(nums, nums[0]))
# @lc code=end

print(Solution().countElements([1,1,1,1,2,2,3]))