#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
from typing import List
def dp(dd):
    def _dp(func):
        def ret(self,a,b):
            if (a,b) in dd:return dd[(a,b)]
            tmp=func(self,a,b)
            dd[(a,b)]=tmp
            return tmp
        return ret
    return _dp  
class Solution:
    dd={}
    @dp(dd)
    def func(self,x:int,y:int)->int:
        if x>=self.m or y>=self.n or self.mat[x][y]:return 0
        if x==self.m-1 and y==self.n-1:return 1
        return self.func(x+1,y)+self.func(x,y+1)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.m,self.n,self.mat=len(obstacleGrid),len(obstacleGrid[0]),obstacleGrid
        self.dd.clear()
        return self.func(0,0)
# @lc code=end

