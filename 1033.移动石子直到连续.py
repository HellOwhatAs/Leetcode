#
# @lc app=leetcode.cn id=1033 lang=python3
#
# [1033] 移动石子直到连续
#

# @lc code=start
from typing import List
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted((a, b, c))
        if b - a == c - b == 1: return [0, 0]
        if b - a <= 2 or c - b <= 2: return [1, c - a - 2]
        return [2, c - a - 2]
# @lc code=end

print(Solution().numMovesStones(a = 1, b = 2, c = 5))
print(Solution().numMovesStones(a = 4, b = 3, c = 2))
print(Solution().numMovesStones(3, 5, 1))