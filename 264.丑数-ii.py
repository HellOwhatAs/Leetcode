#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
from typing import Tuple
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        pq, pq_set = [1], {1}
        for _ in range(n):
            ret = heapq.heappop(pq)
            pq_set.remove(ret)
            for factor in (2, 3, 5):
                if (tmp := ret * factor) in pq_set: continue
                heapq.heappush(pq, tmp)
                pq_set.add(tmp)
        return ret
# @lc code=end

print(Solution().nthUglyNumber(n = 10))