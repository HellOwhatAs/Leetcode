#
# @lc app=leetcode.cn id=2050 lang=python3
#
# [2050] 并行课程 III
#

# @lc code=start
from typing import List
from collections import deque
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adjlist = [[] for _ in range(n)]
        in_degrees = [0] * n
        for s, t in relations:
            adjlist[s-1].append(t-1)
            in_degrees[t-1] += 1
        q = deque([i for i, degree in enumerate(in_degrees) if degree == 0])
        earlist = [time[i] if degree == 0 else 0 for i, degree in enumerate(in_degrees)]
        while q:
            cur = q.popleft()
            for neibour in adjlist[cur]:
                in_degrees[neibour] -= 1
                earlist[neibour] = max(earlist[neibour], earlist[cur] + time[neibour])
                if in_degrees[neibour] == 0:
                    q.append(neibour)
        return max(earlist)
        

# @lc code=end

print(Solution().minimumTime(n = 3, relations = [[1,3],[2,3]], time = [3,2,5]))
print(Solution().minimumTime(n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5]))