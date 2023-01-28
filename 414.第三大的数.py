#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# @lc code=start
from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ns = set(nums)
        max1 = max(ns)
        ns.remove(max1)
        if not ns: return max1
        max2 = max(ns)
        ns.remove(max2)
        if not ns: return max1
        max3 = max(ns)
        return max3
# @lc code=end

print(Solution().thirdMax([2, 2, 3, 1]))