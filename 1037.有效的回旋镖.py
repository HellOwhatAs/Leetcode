#
# @lc app=leetcode.cn id=1037 lang=python3
#
# [1037] 有效的回旋镖
#

# @lc code=start
from typing import List
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        (x0, y0), (x1, y1), (x2, y2) = points
        return (x0 != x1 or y0 != y1) and (x1 != x2 or y1 != y2) and (x2!=x0 or y2 != y0) and (y1-y0)*(x2-x1) != (y2-y1)*(x1-x0)
# @lc code=end

