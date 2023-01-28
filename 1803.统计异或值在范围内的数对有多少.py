#
# @lc app=leetcode.cn id=1803 lang=python3
#
# [1803] 统计异或值在范围内的数对有多少
#

# @lc code=start
from typing import List
from collections import Counter
class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        ans, cnt = 0, Counter(nums)
        high += 1
        while high:
            nxt = Counter()
            for x, c in cnt.items():
                ans += c * (high % 2 * cnt[(high - 1) ^ x] - low % 2 * cnt[(low - 1) ^ x])
                nxt[x >> 1] += c
            cnt = nxt
            low >>= 1
            high >>= 1
        return ans // 2
# @lc code=end
