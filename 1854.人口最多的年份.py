#
# @lc app=leetcode.cn id=1854 lang=python3
#
# [1854] 人口最多的年份
#

# @lc code=start
from typing import List
import heapq
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs.sort()
        heap, max_pop, max_year = [], 0, None
        for birth, death in logs:
            while heap and heap[0] <= birth:
                heapq.heappop(heap)
            heapq.heappush(heap, death)
            if len(heap) > max_pop:
                max_year, max_pop = birth, len(heap)
        return max_year
        
# @lc code=end
print(Solution().maximumPopulation([[1993,1999],[2000,2010]]))