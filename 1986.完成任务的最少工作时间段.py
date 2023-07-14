#
# @lc app=leetcode.cn id=1986 lang=python3
#
# [1986] 完成任务的最少工作时间段
#

# @lc code=start
from typing import List, Tuple
from itertools import product
from math import inf
class Solution:
    @staticmethod
    def func(o: Tuple[int, int], x: int, sessionTime: int) -> Tuple[int, int]:
        if o[1] + x <= sessionTime: return o[0], o[1] + x
        return o[0] + 1, x
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        dp = [(inf, inf)] * (1<<n)
        dp[0] = 1, 0
        for key, i in product(range(1, 1<<n), range(n)):
            if not (key & (1<<i)): continue
            dp[key] = min(dp[key], self.func(dp[key ^ (1<<i)], tasks[i], sessionTime))
        return dp[-1][0]

# @lc code=end

print(Solution().minSessions(tasks = [1,2,3], sessionTime = 3))
print(Solution().minSessions(tasks = [3,1,3,1,1], sessionTime = 8))
print(Solution().minSessions(tasks = [1,2,3,4,5], sessionTime = 15))
print(Solution().minSessions([1,1,2,2,2,2,3,3,6,6,6,6], 10))