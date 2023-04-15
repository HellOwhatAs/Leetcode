#
# @lc app=leetcode.cn id=1042 lang=python3
#
# [1042] 不邻接植花
#

# @lc code=start
from typing import List
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for a, b in paths:
            adj[a - 1].append(b - 1)
            adj[b - 1].append(a - 1)
        ans = [0] * n
        for i in range(n):
            colored = [False] * 5
            for vertex in adj[i]:
                colored[ans[vertex]] = True
            for j in range(1, 5):
                if not colored[j]:
                    ans[i] = j
                    break
        return ans
# @lc code=end

