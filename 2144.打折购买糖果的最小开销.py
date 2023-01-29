#
# @lc app=leetcode.cn id=2144 lang=python3
#
# [2144] 打折购买糖果的最小开销
#

# @lc code=start
from typing import List
import heapq
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost, ret = [-i for i in cost], 0
        heapq.heapify(cost)
        while len(cost) > 2:
            ret -= heapq.heappop(cost) + heapq.heappop(cost)
            heapq.heappop(cost)
        return ret - sum(cost)
# @lc code=end

print(Solution().minimumCost([15,5]))