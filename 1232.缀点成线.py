#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#

# @lc code=start
from typing import List
from fractions import Fraction
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates.pop()
        ks = [Fraction(y1-y0, x1-x0) if x1!=x0 else float('inf') for x1, y1 in coordinates]
        return max(ks) == min(ks)
# @lc code=end

