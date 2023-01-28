#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
from typing import List
def mycache(dd:dict):
    def _mycache(func):
        def ret(self,a:int,b:int):
            if (a,b) in dd:return dd[(a,b)]
            tmp=func(self,a,b)
            dd[(a,b)]=tmp
            return tmp
        return ret
    return _mycache
class Solution:
    dd={}
    @mycache(dd)
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [] if n<k else [tuple(range(1,n+1))] if n==k else [(i,) for i in range(1,n+1)] if k==1 else [j+(i,) for i in range(1,n+1) for j in self.combine(i-1,k-1)]
# @lc code=end