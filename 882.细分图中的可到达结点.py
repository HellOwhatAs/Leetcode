#
# @lc app=leetcode.cn id=882 lang=python3
#
# [882] 细分图中的可到达结点
#

# @lc code=start
from typing import List
from collections import defaultdict
import heapq
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        adList = defaultdict(list)
        for u, v, nodes in edges:
            adList[u].append([v, nodes])
            adList[v].append([u, nodes])
        used = {}
        visited = set()
        reachableNodes = 0
        pq = [[0, 0]]

        while pq and pq[0][0] <= maxMoves:
            step, u = heapq.heappop(pq)
            if u in visited:
                continue
            visited.add(u)
            reachableNodes += 1
            for v, nodes in adList[u]:
                if nodes + step + 1 <= maxMoves and v not in visited:
                    heapq.heappush(pq, [nodes + step + 1, v])
                used[(u, v)] = min(nodes, maxMoves - step)

        for u, v, nodes in edges:
            reachableNodes += min(nodes, used.get((u, v), 0) + used.get((v, u), 0))
        return reachableNodes
# @lc code=end

