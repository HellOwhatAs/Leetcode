#
# @lc app=leetcode.cn id=2148 lang=python3
#
# [2148] 元素计数
#

# @lc code=start
from typing import List
class Solution:
    def countElements(self, nums: List[int]) -> int:
        nmax, nmin = max(nums), min(nums)
        return sum(nmin< i < nmax for i in nums)
# @lc code=end

print(Solution().countElements([1,1,1,1,2,2,3]))