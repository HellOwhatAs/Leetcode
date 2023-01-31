#
# @lc app=leetcode.cn id=1464 lang=python3
#
# [1464] 数组中两元素的最大乘积
#

# @lc code=start
from typing import List
from heapq import nlargest
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a, b = nlargest(2, nums)
        return (a - 1) * (b - 1)
# @lc code=end

