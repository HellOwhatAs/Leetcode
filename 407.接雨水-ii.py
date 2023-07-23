#
# @lc app=leetcode.cn id=407 lang=python3
#
# [407] 接雨水 II
#

# @lc code=start
from typing import List
import heapq
class Solution:
    def neibours(self, i, j, m, n):
        for i1, j1 in (            (i, j-1), 
                       (i-1, j),             (i+1, j),
                                   (i, j+1)):
            if 0 <= i1 < m and 0 <= j1 < n: yield (i1, j1)

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        water, vis = [], {}
        for i in range(m):
            water.append((heightMap[i][0], i, 0))
            water.append((heightMap[i][-1], i, n - 1))
            vis[(i, 0)] = heightMap[i][0]
            vis[(i, n - 1)] = heightMap[i][-1]
        for j in range(1, n - 1):
            water.append((heightMap[0][j], 0, j))
            water.append((heightMap[-1][j], m - 1, j))
            vis[(0, j)] = heightMap[0][j]
            vis[(m - 1, j)] = heightMap[-1][j]
        heapq.heapify(water)

        while len(vis) < m * n:
            height, i, j = heapq.heappop(water)
            for i1, j1 in self.neibours(i, j, m, n):
                if (i1, j1) in vis: continue
                heapq.heappush(water, (max(height, heightMap[i1][j1]), i1, j1))
                vis[(i1, j1)] = max(height, heightMap[i1][j1])
        
        return sum(height - heightMap[i][j] for (i, j), height in vis.items())
        
        
# @lc code=end

print(Solution().trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))
print(Solution().trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]))