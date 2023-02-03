#
# @lc app=leetcode.cn id=2391 lang=python3
#
# [2391] 收集垃圾的最少总时间
#

# @lc code=start
from typing import List
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        M, P, G = [], [], []
        for i in garbage:
            M.append(i.count('M'))
            P.append(i.count('P'))
            G.append(i.count('G'))
        while M and M[-1] == 0: M.pop()
        while P and P[-1] == 0: P.pop()
        while G and G[-1] == 0: G.pop()
        ret = (M[0] if M else 0) + (P[0] if P else 0) + (G[0] if G else 0)
        for i in range(1, len(M)):
            ret += travel[i - 1] + M[i]
        for i in range(1, len(P)):
            ret += travel[i - 1] + P[i]
        for i in range(1, len(G)):
            ret += travel[i - 1] + G[i]
        return ret
# @lc code=end

print(Solution().garbageCollection(garbage = ["MMM","PGM","GP"], travel = [3,10]))