#
# @lc app=leetcode.cn id=1000 lang=python3
#
# [1000] 合并石头的最低成本
#

# @lc code=start
from typing import List
from collections import defaultdict
class Solution:
    def func(self, l: int, r: int, t: int) -> int:
        if l >= r: return self.dp[l, r, t]
        if (l, r, t) in self.dp: return self.dp[l, r, t]
        if t == 1: ret = self.func(l, r, self.k) + sum(self.stones[i] for i in range(l, r + 1))
        else: ret = min(self.func(l, p, 1) + self.func(p + 1, r, t - 1) for p in range(l, r))
        self.dp[l, r, t] = ret
        return ret
    def mergeStones(self, stones: List[int], k: int) -> int:
        self.stones, self.k, self.n = stones, k, len(stones)
        self.dp = defaultdict(lambda:float('inf'))
        for i in range(self.n): self.dp[i, i, 1] = 0
        ret = self.func(0, self.n - 1, 1)
        return -1 if ret == float('inf') else ret
# @lc code=end

print(Solution().mergeStones(stones = [3,2,4,1], k = 2))
print(Solution().mergeStones(stones = [3,2,4,1], k = 3))
print(Solution().mergeStones(stones = [3,5,1,2,6], k = 3))
