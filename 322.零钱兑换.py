#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
from typing import List
from math import inf, isinf
from functools import lru_cache

class Solution:
    @lru_cache(None)
    def func(self, amount: int) -> int:
        return 1 + min(self.func(amount - coin) for coin in self.coins) if amount > 0 else (inf if amount < 0 else 0)
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        ret = self.func(amount)
        return -1 if isinf(ret) else ret
# @lc code=end

print(Solution().coinChange(coins = [1, 2, 5], amount = 11))
print(Solution().coinChange(coins = [2], amount = 3))
print(Solution().coinChange(coins = [1], amount = 0))