#
# @lc app=leetcode.cn id=1223 lang=python3
#
# [1223] 掷骰子模拟
#

# @lc code=start
from typing import List
from itertools import product
import pprint
class Solution:
    MOD = 10 ** 9 + 7
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[[0] * 16 for _ in range(6)] for _ in range(n + 1)]
        for j in range(6): dp[1][j][1] = 1
        for i in range(2, n + 1):
            t = i & 1
            for j in range(6): dp[t][j] = [0] * 16
            for j in range(6):
                for k, p in product(range(1, rollMax[j] + 1), range(6)):
                    if p != j:
                        dp[t][p][1] = (dp[t][p][1] + dp[t ^ 1][j][k]) % self.MOD
                    elif k + 1 <= rollMax[j]:
                        dp[t][p][k + 1] = (dp[t][p][k + 1] + dp[t ^ 1][j][k]) % self.MOD
        res = 0
        for j in range(6):
            for k in range(1, rollMax[j] + 1):
                res = (res + dp[n & 1][j][k]) % self.MOD
        return res
# @lc code=end

print(Solution().dieSimulator(4, [2,1,1,3,3,2]))