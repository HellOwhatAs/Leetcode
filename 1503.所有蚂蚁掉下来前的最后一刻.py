#
# @lc app=leetcode.cn id=1503 lang=python3
#
# [1503] 所有蚂蚁掉下来前的最后一刻
#

# @lc code=start
from typing import List
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left, default=0), n - min(right, default=n))
# @lc code=end

