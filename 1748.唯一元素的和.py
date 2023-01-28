#
# @lc app=leetcode.cn id=1748 lang=python3
#
# [1748] 唯一元素的和
#

# @lc code=start
from typing import List
from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(k for k, v in Counter(nums).items() if v == 1)
# @lc code=end

print(Solution().sumOfUnique([1,2,3,4,5]))