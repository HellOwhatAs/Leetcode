from typing import List
from array import array

class DSU:
    def __init__(self, n: int):
        self.array = array('i', [-1] * n)
    def find(self, x: int):
        if self.array[x] < 0: return x
        self.array[x] = self.find(self.array[x])
        return self.array[x]
    def query(self, a: int, b: int):
        return self.find(a) == self.find(b)
    def union(self, a: int, b: int):
        a, b = self.find(a), self.find(b)
        if a == b: return
        if self.array[a] >= self.array[b]:
            a, b = b, a
        self.array[a] += self.array[b]
        self.array[b] = a

class Solution:
    def union(self, _i: int, _j: int):
        for i in range(max(0, _i - 1), min(self.m, _i + 2)):
            for j in range(max(0, _j - 1), min(self.n, _j + 2)):
                if i == _i and j == _j: continue
                if self.land[i][j] == 0:
                    self.dsu.union(_i * self.n + _j, i * self.n + j)

    def pondSizes(self, land: List[List[int]]) -> List[int]:
        self.m, self.n = len(land), len(land[0])
        self.land = land
        self.dsu = DSU(self.m * self.n)
        for i in range(self.m):
            for j in range(self.n):
                if self.land[i][j] == 0:
                    self.union(i, j)
        return sorted(-elem for elem, land_item in zip(self.dsu.array, sum(land, [])) if elem < 0 and land_item == 0)