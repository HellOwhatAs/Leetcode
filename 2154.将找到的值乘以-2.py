#
# @lc app=leetcode.cn id=2154 lang=python3
#
# [2154] 将找到的值乘以 2
#

# @lc code=start
from typing import List
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        s = set(nums)
        while original in s:
            original *= 2
        return original
# @lc code=end

print(Solution().findFinalValue(nums = [2,7,9], original = 4))