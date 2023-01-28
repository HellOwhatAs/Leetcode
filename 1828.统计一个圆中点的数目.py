#
# @lc app=leetcode.cn id=1828 lang=python3
#
# [1828] 统计一个圆中点的数目
#

# @lc code=start
from typing import List
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for x0, y0, r in queries:
            tmp = 0
            for x, y in points:
                if (x-x0)**2 + (y-y0)**2 <= r**2: tmp+=1
            ans.append(tmp)
        return ans
# @lc code=end

