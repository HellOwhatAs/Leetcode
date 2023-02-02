#
# @lc app=leetcode.cn id=1129 lang=python3
#
# [1129] 颜色交替的最短路径
#

# @lc code=start
from typing import List
from queue import Queue
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        answer = [-1] * n
        answer[0] = 0
        edges = [[[] for _ in range(n)], [[] for _ in range(n)]]
        for s, e in redEdges: edges[0][s].append(e)
        for s, e in blueEdges: edges[1][s].append(e)
        q = Queue()
        q.put((0, 0, 0))
        q.put((0, 1, 0))
        vis = set()
        while not q.empty():
            idx, color, dis = q.get()
            vis.add((idx, color))
            if answer[idx] == -1 or answer[idx] > dis:
                answer[idx] = dis
            notcolor = int(not color)
            for e in edges[notcolor][idx]:
                if not (e, notcolor) in vis:
                    q.put((e, notcolor, dis + 1))
        return answer
# @lc code=end

print(Solution().shortestAlternatingPaths(5,
[[0,1],[1,2],[2,3],[3,4]],
[[1,2],[2,3],[3,1]]))