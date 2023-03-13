#
# @lc app=leetcode.cn id=1617 lang=python3
#
# [1617] 统计子树中城市之间最大距离
#

# @lc code=start
from typing import List
from itertools import product
from math import inf
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        dist = [[inf] * n for _ in range(n)]
        for i in range(n): dist[i][i] = 0
        for x, y in edges:
            x, y = x - 1, y - 1
            adj[x].append(y)
            adj[y].append(x)
            dist[x][y] = dist[y][x] = 1
        for i, j, k in product(*[range(n)] * 3):
            if dist[j][j] != inf and dist[i][k] != inf:
                dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])
        ans = [0] * (n - 1)
        for i in range(n - 1):
            for j in range(i + 1, n):
                ans[dist[i][j] - 1] += self.dfs(adj, dist, i, -1, i, j)
        return ans
    def dfs(self, adj: List[List[int]], dist: List[List[int]], u: int, parent: int, x: int, y: int):
        if (dist[u][x] > dist[x][y] or dist[u][y] > dist[x][y]) or ((dist[u][y] == dist[x][y] and u < x) or (dist[u][x] == dist[x][y] and u < y)): return 1
        ret = 1
        for v in adj[u]:
            if v != parent: ret *= self.dfs(adj, dist, v, u, x, y)
        if dist[u][x] + dist[u][y] > dist[x][y]: ret += 1
        return ret
# @lc code=end

print(Solution().countSubgraphsForEachDiameter(n = 4, edges = [[1,2],[2,3],[2,4]]))
print(Solution().countSubgraphsForEachDiameter(n = 2, edges = [[1,2]]))
print(Solution().countSubgraphsForEachDiameter(n = 3, edges = [[1,2],[2,3]]))