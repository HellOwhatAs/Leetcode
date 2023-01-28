#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
from typing import List
from functools import lru_cache
class Solution:
    @lru_cache
    def lmax(self,x:int)->int:
        if x==0:return self.height[x]
        return max(self.lmax(x-1),self.height[x])
    @lru_cache
    def rmax(self,x:int)->int:
        if x==len(self.height)-1:return self.height[x]
        return max(self.height[x],self.rmax(x+1))
    def trap(self, height: List[int]) -> int:
        self.height=height
        ret=0
        for i in range(1,len(self.height)-1):
            ret+=min(self.lmax(i),self.rmax(i))-self.height[i]
        return ret
# @lc code=end

