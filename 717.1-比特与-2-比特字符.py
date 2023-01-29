#
# @lc app=leetcode.cn id=717 lang=python3
#
# [717] 1 比特与 2 比特字符
#

# @lc code=start
from typing import List
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def func(self, end: int) -> bool:
        if end == 0: return self.bits[0] == 0
        if end == 1: return self.bits[1] == 0 or self.bits[0] == 1
        if self.bits[end] == 0:
            return self.func(end - 1) or self.bits[end - 1] == 1 and self.func(end - 2)
        else:
            return self.bits[end - 1] == 1 and self.func(end - 2)
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        if n == 1 or bits[-2] == 0: return True
        if n == 2: return bits[0] != 1
        self.bits = bits
        return self.func(n - 2)
# @lc code=end

print(Solution().isOneBitCharacter([1,1,0]))