#
# @lc app=leetcode.cn id=834 lang=python3
#
# [834] 树中距离之和
#

# @lc code=start
from typing import List, Optional
class Solution:
    def adjlist2tree(self, start: int, father: Optional[int] = None):
        if father in self.tree[start]: self.tree[start].remove(father)
        for t in self.tree[start]: self.adjlist2tree(t, start)
    
    def dfs0(self, start: int):
        for t in self.tree[start]:
            self.dfs0(t)
            self.sz[start] += self.sz[t]
            self.dp[start] += self.dp[t] + self.sz[t]
        
    def swap_root(self, child: int, root: int):
        '''assuming `dp` and `sz` are initialized with `root` being root'''
        __backup__ = self.dp[root], self.dp[child], self.sz[root], self.sz[child]
        self.dp[root] -= self.dp[child] + self.sz[child]
        self.sz[root] -= self.sz[child]
        self.sz[child] += self.sz[root]
        self.dp[child] += self.dp[root] + self.sz[root]
        
        self.ret[child] = self.dp[child]
        for child1 in self.tree[child]:
            self.swap_root(child1, child)

        self.dp[root], self.dp[child], self.sz[root], self.sz[child] = __backup__

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.tree = [set() for _ in range(n)]
        for s, t in edges: self.tree[s].add(t), self.tree[t].add(s)
        self.adjlist2tree(0)
        
        self.dp, self.sz, self.ret = [0] * n, [1] * n, [None] * n
        self.dfs0(0)
        self.ret[0] = self.dp[0]

        for child in self.tree[0]:
            self.swap_root(child, 0)

        return self.ret

# @lc code=end

print(Solution().sumOfDistancesInTree(n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]))
print(Solution().sumOfDistancesInTree(n = 1, edges = []))
print(Solution().sumOfDistancesInTree(n = 2, edges = [[1,0]]))