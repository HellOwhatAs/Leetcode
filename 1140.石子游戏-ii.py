#
# @lc app=leetcode.cn id=1140 lang=python3
#
# [1140] 石子游戏 II
#

# @lc code=start
from typing import List
from itertools import product
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp, s = [[0] * (n + 1) for _ in range(n)], [0] * (n + 1)
        for i in reversed(range(n)):
            s[i] = s[i + 1] + piles[i]
        for i, M in product(reversed(range(n)), range(1, n + 1)):
            dp[i][M] = s[i] if i + 2 * M >= n else max(dp[i][M], max(s[i] - dp[i + x][max(M, x)] for x in range(1, 2 * M + 1)))
        return dp[0][1]
# @lc code=end

print(Solution().stoneGameII([2, 7, 9, 4, 4]))