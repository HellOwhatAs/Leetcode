#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
from typing import List
class Solution:
    def judge(self,x:List[int]):
        for i in range(len(x)):
            for j in range(i+1,len(x)):
                if x[i]==x[j]:return False
                if abs(j-i)==abs(x[i]-x[j]):return False
        return True
    def int2str(self,i:int):
        return "."*i+"Q"+"."*(self.n-i-1)
    def func(self,x:List[List[int]]):
        return [i+[j] for i in x for j in range(self.n) if not j in i and self.judge(i+[j])]
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n=n
        ret=[[i] for i in range(n)]
        for i in range(n-1):ret=self.func(ret)
        return [[self.int2str(j) for j in i] for i in ret]
    def totalNQueens(self, n: int) -> int:
        self.n=n
        ret=[[i] for i in range(n)]
        for i in range(n-1):ret=self.func(ret)
        return len(ret)
# @lc code=end

