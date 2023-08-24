#
# @lc app=leetcode.cn id=1267 lang=python3
#
# [1267] 统计参与通信的服务器
#

# @lc code=start
from typing import List
from itertools import product

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        return (
            sum(sum(row) for row in grid) - 
            sum(grid[i][j] for i, j in product(
                (i for i in range(m) if sum(grid[i]) == 1),
                (j for j in range(n) if sum(grid[i][j] for i in range(m)) == 1)))
        )
# @lc code=end

print(Solution().countServers(grid = [[1,0],[0,1]]))
print(Solution().countServers(grid = [[1,0],[1,1]]))
print(Solution().countServers(grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))