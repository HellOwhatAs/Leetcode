#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
from math import sqrt, inf
from functools import lru_cache

class Solution:
    @lru_cache(None)
    def numSquares(self, n: int) -> int:
        if n == 0: return 0
        return 1 + min(self.numSquares(n - i ** 2) for i in reversed(range(1, int(sqrt(n)) + 1)))

# @lc code=end

print(Solution().numSquares(n = 12))
print(Solution().numSquares(n = 13))
print(Solution().numSquares(7168))