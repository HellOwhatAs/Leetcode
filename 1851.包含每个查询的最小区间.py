#
# @lc app=leetcode.cn id=1851 lang=python3
#
# [1851] 包含每个查询的最小区间
#

# @lc code=start
from typing import List
import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        order = sorted(range(len(queries)), key=lambda x: queries[x])
        pq = []
        ret = [-1] * len(queries)
        idx = 0
        for i in order:
            while idx < len(intervals) and intervals[idx][0] <= queries[i]:
                heapq.heappush(pq, (intervals[idx][1] - intervals[idx][0] + 1, intervals[idx][1]))
                idx += 1
            while pq and pq[0][1] < queries[i]:
                heapq.heappop(pq)
            if pq:
                ret[i] = pq[0][0]
        return ret
# @lc code=end

print(Solution().minInterval(intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]))
print(Solution().minInterval(intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]))