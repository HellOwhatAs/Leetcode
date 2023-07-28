#
# @lc app=leetcode.cn id=1494 lang=python3
#
# [1494] 并行课程 II
#

# @lc code=start
from typing import List, Dict
from itertools import combinations
from math import inf

def cache(d: Dict):
    def wrapper(func):
        def myfunc(self, in_degrees: List[int], vis: int):
            key = vis
            if key in d: return d[key]
            val = func(self, in_degrees, vis)
            d[key] = val
            return val
        return myfunc
    return wrapper

class Solution:
    d = {}
    @cache(d)
    def dfs(self, in_degrees: List[int], vis: int) -> int:
        if vis == 0: return 0
        starts = [i for i, deg in enumerate(in_degrees) if deg == 0 and vis & (1<<i)]
        ret = inf
        for candis in combinations(starts, min(len(starts), self.k)):
            for cur in candis:
                vis &= ~(1<<cur)
                for neibour in self.adjlist[cur]:
                    in_degrees[neibour] -= 1
            ret = min(ret, self.dfs(in_degrees, vis))
            for cur in candis:
                vis |= (1<<cur)
                for neibour in self.adjlist[cur]:
                    in_degrees[neibour] += 1
        return ret + 1

    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        self.d.clear()
        self.adjlist = adjlist = [[] for _ in range(n)]
        self.k = k
        in_degrees = [0] * n
        for s, t in relations:
            adjlist[s-1].append(t-1)
            in_degrees[t-1] += 1
        
        return self.dfs(in_degrees, (1<<n)-1)


# @lc code=end

print(Solution().minNumberOfSemesters(n = 4, relations = [[2,1],[3,1],[1,4]], k = 2))
print(Solution().minNumberOfSemesters(n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2))
print(Solution().minNumberOfSemesters(n = 11, relations = [], k = 2))
print(Solution().minNumberOfSemesters(13, [[12,8],[2,4],[3,7],[6,8],[11,8],[9,4],[9,7],[12,4],[11,4],[6,4],[1,4],[10,7],[10,4],[1,7],[1,8],[2,7],[8,4],[10,8],[12,7],[5,4],[3,4],[11,7],[7,4],[13,4],[9,8],[13,8]], 9))
print(Solution().minNumberOfSemesters(2, [], 1))