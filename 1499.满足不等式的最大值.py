#
# @lc app=leetcode.cn id=1499 lang=python3
#
# [1499] 满足不等式的最大值
#

# @lc code=start
from typing import List
from collections import deque
from math import inf
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = deque()
        ret = -inf
        for j in range(len(points)):
            xj, yj = points[j]
            while q and xj - points[q[0]][0] > k:
                q.popleft()
            if q:
                xi, yi = points[q[0]]
                ret = max(ret, xj + yj + yi - xi)
            while q and points[q[-1]][1] - points[q[-1]][0] < yj - xj:
                q.pop()
            q.append(j)
        return ret
# @lc code=end

print(Solution().findMaxValueOfEquation(points = [[1,3],[2,0],[5,10],[6,-10]], k = 1))
print(Solution().findMaxValueOfEquation(points = [[0,0],[3,0],[9,2]], k = 3))