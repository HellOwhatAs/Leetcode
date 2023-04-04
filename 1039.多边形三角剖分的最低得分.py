#
# @lc app=leetcode.cn id=1039 lang=python3
#
# [1039] 多边形三角剖分的最低得分
#

# @lc code=start
from typing import List
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def func(self, start: int, end: int) -> int:
        return 0 if end - start < 2 else min(self.func(start, i) + self.func(i, end) + self.values[start] * self.values[end] * self.values[i] for i in range(start + 1, end))
    def minScoreTriangulation(self, values: List[int]) -> int:
        self.n, self.values = len(values), values
        return self.func(0, self.n - 1)
# @lc code=end

print(Solution().minScoreTriangulation(values = [1,2,3]))
print(Solution().minScoreTriangulation(values = [3,7,4,5]))
print(Solution().minScoreTriangulation(values = [1,3,1,4,1,5]))