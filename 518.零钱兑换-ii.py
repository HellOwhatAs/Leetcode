#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start

from typing import List
from math import inf, isinf
from functools import lru_cache

class Solution:
    @lru_cache(None)
    def func(self, start: int, val: int) -> int:
        if start == len(self.coins): return val == 0
        if val < 0: return 0
        return sum(
            self.func(start + 1, val - num * self.coins[start])
            for num in range(val // self.coins[start] + 1)
        )

    def change(self, amount: int, coins: List[int]) -> int:
        self.coins = coins
        return self.func(0, amount)
# @lc code=end

print(Solution().change(amount = 5, coins = [1, 2, 5]))
print(Solution().change(amount = 3, coins = [2]))
print(Solution().change(amount = 10, coins = [10] ))