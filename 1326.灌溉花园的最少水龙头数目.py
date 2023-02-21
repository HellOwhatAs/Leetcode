#
# @lc app=leetcode.cn id=1326 lang=python3
#
# [1326] 灌溉花园的最少水龙头数目
#

# @lc code=start
from typing import List
from math import inf
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = sorted((max(0, i - r), min(n, i + r)) for i, r in enumerate(ranges))
        dp = [inf] * (n + 1)
        dp[0] = 0
        for start, end in intervals:
            if dp[start] == inf: return -1
            for j in range(start, end + 1):
                dp[j] = min(dp[j], dp[start] + 1)
        return dp[n]
# @lc code=end

print(Solution().minTaps(n = 5, ranges = [3,4,1,1,0,0]))