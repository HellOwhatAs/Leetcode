#
# @lc app=leetcode.cn id=1637 lang=python3
#
# [1637] 两点之间不包含任何点的最宽垂直面积
#

# @lc code=start
from typing import List
from itertools import pairwise
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        return max((0, *(x1 - x0 for x0, x1 in pairwise(sorted(set(x for x, y in points))))))
# @lc code=end

print(Solution().maxWidthOfVerticalArea(points = [[8,7],[9,9],[7,4],[9,7]]))
print(Solution().maxWidthOfVerticalArea(points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))
print(Solution().maxWidthOfVerticalArea([[1,1],[1,2],[1,3]]))