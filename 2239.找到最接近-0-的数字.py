#
# @lc app=leetcode.cn id=2239 lang=python3
#
# [2239] 找到最接近 0 的数字
#

# @lc code=start
from typing import List
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        return tmp if (tmp:=min(nums, key=lambda x: abs(x))) > 0 else tmp if not -tmp in nums else -tmp
# @lc code=end

print(Solution().findClosestNumber([2,-1,1]))