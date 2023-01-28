#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
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
        if x==self.m-1 or y==self.n-1:return 1
        return self.func(x+1,y)+self.func(x,y+1)
    def uniquePaths(self, m: int, n: int) -> int:
        self.m,self.n=m,n
        self.dd.clear()
        return self.func(0,0)
# @lc code=end

