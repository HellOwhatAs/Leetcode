#
# @lc app=leetcode.cn id=1971 lang=python3
#
# [1971] 寻找图中是否存在路径
#

# @lc code=start
from typing import List
class bxjj:
    def __init__(self, l:int):
        self.length=l
        self.data=[-1]*l
    def father(self, x:int)->int:
        if(self.data[x]<0):return x
        self.data[x]=self.father(self.data[x])
        return self.data[x]
    def hb(self, a:int, b:int):
        a=self.father(a)
        b=self.father(b)
        if(a==b):return
        if(self.data[a]<self.data[b]):
            self.data[a]+=self.data[b]
            self.data[b]=a
        else:
            self.data[b]+=self.data[a]
            self.data[a]=b
    def cha(self, a:int, b:int)->bool:
        return self.father(a)==self.father(b)
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        a=bxjj(n)
        for i,j in edges:a.hb(i,j)
        return a.cha(source, destination)
# @lc code=end

