#
# @lc app=leetcode.cn id=1615 lang=python3
#
# [1615] 最大网络秩
#

# @lc code=start
from typing import List
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        data: List[List[int]] = [[] for _ in range(n)]
        for a, b in roads: data[a].append(b), data[b].append(a)
        return max(max(len(data[i]) + len(data[j]) - (i in data[j]) for j in range(i + 1, n)) for i in range(n - 1))
# @lc code=end

print(Solution().maximalNetworkRank(n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]))
print(Solution().maximalNetworkRank(n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]))
print(Solution().maximalNetworkRank(n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]))
print(Solution().maximalNetworkRank(2, [[1,0]]))
print(Solution().maximalNetworkRank(5, [[2,3],[0,3],[0,4],[4,1]]))