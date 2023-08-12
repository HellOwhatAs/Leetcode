#
# @lc app=leetcode.cn id=990 lang=python3
#
# [990] 等式方程的可满足性
#

# @lc code=start
from typing import List, Dict

class DisjointSet:
    def __init__(self, _size) -> None:
        self.size = _size
        self.data = [-1] * _size
    
    def query(self, val: int) -> int:
        if self.data[val] < 0: return val
        self.data[val] = self.query(self.data[val])
        return self.data[val]

    def merge(self, a: int, b: int) -> None:
        root_a, root_b = self.query(a), self.query(b)
        if root_a == root_b: return
        if self.data[root_a] < self.data[root_b]: root_a, root_b = root_b, root_a
        self.data[root_a], self.data[root_b] = self.data[root_a] + self.data[root_b], root_a

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        idxer: Dict[str, int] = {}
        for eq in equations:
            if eq[0] not in idxer: idxer[eq[0]] = len(idxer)
            if eq[3] not in idxer: idxer[eq[3]] = len(idxer)
        djs = DisjointSet(len(idxer))
        for eq in equations:
            if eq[1] == '!': continue
            djs.merge(idxer[eq[0]], idxer[eq[3]])
        for eq in equations:
            if eq[1] == '!' and djs.query(idxer[eq[0]]) == djs.query(idxer[eq[3]]):
                return False
        return True
# @lc code=end

