#
# @lc app=leetcode.cn id=980 lang=python3
#
# [980] 不同路径 III
#

# @lc code=start
from typing import List
from functools import lru_cache

class Solution:

    def search(self, val: int):
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == val:
                    return i, j
    
    def count(self, val: int):
        return sum(self.grid[i][j] == val
                   for j in range(self.n)
                   for i in range(self.m))

    def get_state(self, i: int, j: int, state: int) -> int:
        return (state >> (i * self.n + j)) & 1
    
    def set_state(self, i: int, j: int, state: int) -> int:
        return state | (1 << (i * self.n + j))
    
    @lru_cache(None)
    def dfs(self, i: int, j: int, state: int) -> int:
        if self.grid[i][j] == 2: return state.bit_count() == self.length
        state = self.set_state(i, j, state)
        ret = 0
        for di, dj in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            i1, j1 = i + di, j + dj
            if (i1 < 0 or i1 >= self.m 
                or j1 < 0 or j1 >= self.n
                or self.grid[i1][j1] == -1
                or self.get_state(i1, j1, state)): continue
            ret += self.dfs(i1, j1, state)
        return ret

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        self.length = self.count(0) + 1
        i, j = self.search(1)
        return self.dfs(i, j, 0)



# @lc code=end

print(Solution().uniquePathsIII([
    [1,0,0,0],
    [0,0,0,0],
    [0,0,2,-1]]))
print(Solution().uniquePathsIII([
    [1,0,0,0],
    [0,0,0,0],
    [0,0,0,2]]))
print(Solution().uniquePathsIII([
    [0,1],
    [2,0]]))