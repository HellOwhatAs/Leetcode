#
# @lc app=leetcode.cn id=1595 lang=python3
#
# [1595] 连通两组点的最小成本
#

# @lc code=start
from typing import List
class Solution:
    def func(self, state, level: int):
        if level == self.size1:
            return 0 if state == (1<<self.size2) - 1 else float('inf')
        if not self.dp[state][level] is None: return self.dp[state][level]
        self.dp[state][level] = min((
            *(self.cost[level][k] + self.func(state | (1 << k), level + 1)
            for k in range(self.size2)),
            *(self.cost[level][k] + self.func(state | (1 << k), level)
            for k in range(self.size2) if not (state & (1<<k)))
        )) # a link can't chosen if it not solve a line or a colomn
        return self.dp[state][level]
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        self.cost = cost
        self.size1, self.size2 = len(cost), len(cost[0])
        self.dp = [[None] * self.size1 for _ in range(1<<self.size2)]
        return self.func(0, 0)

# @lc code=end

print(Solution().connectTwoGroups(cost = [[15, 96], [36, 2]]))
print(Solution().connectTwoGroups(cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]))
print(Solution().connectTwoGroups(cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]))
import numpy as np
np.random.seed(0)
print(Solution().connectTwoGroups(np.random.randint(0, 100, (12, 12)).tolist()))