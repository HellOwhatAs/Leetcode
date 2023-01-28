#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start
from typing import List
class bxjj:
    def __init__(self, l: int) -> None:
        self.data, self.l = [-1]*l, l
    def father(self, x: int) -> int:
        if self.data[x]<0: return x
        self.data[x] = self.father(self.data[x])
        return self.data[x]
    def merge(self, a: int, b: int) -> None:
        a, b = self.father(a), self.father(b)
        if a == b: return
        if self.data[a] < self.data[b]:
            self.data[a] += self.data[b]
            self.data[b] = a
        else:
            self.data[b] += self.data[a]
            self.data[a] = b
    def query(self, a: int, b: int) -> bool:
        return self.father(a) == self.father(b)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        a = bxjj(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    a.merge(i, j)
        ret = 0
        for i in a.data:
            if i < 0: ret += 1
        return ret
# @lc code=end

