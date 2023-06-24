#
# @lc app=leetcode.cn id=1659 lang=python3
#
# [1659] 最大化网格幸福感
#

# @lc code=start
from typing import List, Union
class Solution:
    def func(self, grid: List[List[Union[None, int]]], pos: int, ic: int, ec: int) -> Union[int, None]:
        x, y = pos // self.n, pos % self.n
        if ic > self.introvertsCount or ec > self.extrovertsCount:
            return
        if pos == self.m * self.n:
            return 0
        ################
        key = hash(((tuple(grid[x][:y]), tuple() if x == 0 else tuple(grid[x-1][y:])),
            pos, ic, ec))
        if key in self.cache: return self.cache[key]
        ################
        
        results = []

        grid[x][y] = -1
        d_result = 120
        if x - 1 >= 0:
            if grid[x - 1][y] == 1:
                d_result += 20 - 30
            elif grid[x - 1][y] == -1:
                d_result += -30 - 30
        if y - 1 >= 0:
            if grid[x][y - 1] == 1:
                d_result += 20 - 30
            elif grid[x][y - 1] == -1:
                d_result += -30 - 30
        resultnext = self.func(grid, pos + 1, ic + 1, ec)
        if resultnext is not None: results.append(d_result + resultnext)

        grid[x][y] = 0
        resultnext = self.func(grid, pos + 1, ic, ec)
        if resultnext is not None: results.append(resultnext)

        grid[x][y] = 1
        d_result = 40
        if x - 1 >= 0:
            if grid[x - 1][y] == 1:
                d_result += 20 + 20
            elif grid[x - 1][y] == -1:
                d_result += 20 - 30
        if y - 1 >= 0:
            if grid[x][y - 1] == 1:
                d_result += 20 + 20
            elif grid[x][y - 1] == -1:
                d_result += 20 - 30
        resultnext = self.func(grid, pos + 1, ic, ec + 1)
        if resultnext is not None: results.append(d_result + resultnext)
        
        grid[x][y] = None
        ret = max(results) if results else None

        #################
        self.cache[key] = ret
        ################
        return ret

    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        self.m, self.n = m, n
        self.introvertsCount, self.extrovertsCount = introvertsCount, extrovertsCount
        self.cache = {}
        return self.func([[None]*n for _ in range(m)], 0, 0, 0)
# @lc code=end

print(Solution().getMaxGridHappiness(m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2))
print(Solution().getMaxGridHappiness(m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1))
print(Solution().getMaxGridHappiness(m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0))
print(Solution().getMaxGridHappiness(5, 5, 6, 6))