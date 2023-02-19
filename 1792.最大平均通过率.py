#
# @lc app=leetcode.cn id=1792 lang=python3
#
# [1792] 最大平均通过率
#

# @lc code=start
from typing import List
from heapq import heapify, heapreplace

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        Entry = type('Entry', (), {
            "__init__": lambda self, **kwargs: self.__dict__.update(kwargs),
            "__lt__": lambda self, other: (self.t - self.p) * other.t * (other.t + 1) > (other.t - other.p) * self.t * (self.t + 1)
        })
        h = [Entry(p = p, t = t) for p, t in classes]
        heapify(h)
        for _ in range(extraStudents):
            heapreplace(h, Entry(p = h[0].p + 1, t = h[0].t + 1))
        return sum(e.p / e.t for e in h) / len(h)
# @lc code=end

print(Solution().maxAverageRatio(classes = [[1,2],[3,5],[2,2]], extraStudents = 2))
