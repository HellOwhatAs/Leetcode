#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#

# @lc code=start
from typing import List, Tuple
from collections import defaultdict
from functools import lru_cache

class Solution:
    @lru_cache(None)
    def dfs(self, start: Tuple[int, int]) -> int:
        if start not in self.adjlist: return 1
        return max(
            self.dfs(neibour)
            for neibour in self.adjlist[start[0], start[1]]
        ) + 1

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        self.adjlist = adjlist = defaultdict(list)
        for i in range(1, m):
            for j in range(n):
                if matrix[i-1][j] > matrix[i][j]: adjlist[i, j].append((i-1, j))
                elif matrix[i-1][j] < matrix[i][j]: adjlist[i-1, j].append((i, j))
        for i in range(m):
            for j in range(1, n):
                if matrix[i][j-1] > matrix[i][j]: adjlist[i, j].append((i, j-1))
                elif matrix[i][j-1] < matrix[i][j]: adjlist[i, j-1].append((i, j))
        return max(
            (self.dfs(candidates)
            for candidates in adjlist),
            default=1
        )

# @lc code=end

print(Solution().longestIncreasingPath(matrix = [[9,9,4],[6,6,8],[2,1,1]]))
print(Solution().longestIncreasingPath(matrix = [[3,4,5],[3,2,6],[2,2,1]]))
print(Solution().longestIncreasingPath(matrix = [[1]]))