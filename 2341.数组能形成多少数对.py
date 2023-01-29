#
# @lc app=leetcode.cn id=2341 lang=python3
#
# [2341] 数组能形成多少数对
#

# @lc code=start
from typing import List
from collections import Counter
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return [sum(i//2 for i in c.values()), sum(i%2 for i in c.values())]
# @lc code=end

print(Solution().numberOfPairs([0]))