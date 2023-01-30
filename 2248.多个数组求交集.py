#
# @lc app=leetcode.cn id=2248 lang=python3
#
# [2248] 多个数组求交集
#

# @lc code=start
from typing import List
from functools import reduce
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        return sorted(reduce(set.__and__, map(set, nums)))
# @lc code=end

print(Solution().intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))