#
# @lc app=leetcode.cn id=2374 lang=python3
#
# [2374] 边积分最高的节点
#

# @lc code=start
from typing import List
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        ret = [0] * len(edges)
        for ii, i in enumerate(edges):
            ret[i] += ii
        return max(range(len(edges)), key=lambda i: ret[i])
# @lc code=end

print(Solution().edgeScore([2,0,0,2]))