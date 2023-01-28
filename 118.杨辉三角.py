#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
from typing import List
def mycache(dd):
    def _mycache(func):
        def ret(self,n):
            if n in dd:return dd[n]
            tmp=func(self,n)
            dd[n]=tmp
            return tmp
        return ret
    return _mycache
class Solution:
    dd={}
    @mycache(dd)
    def func(self,n:int)->List[int]:
        if n==1:return [1]
        tmp=self.func(n-1)
        ret=[tmp[0]]
        for i in range(1,len(tmp)):ret.append(tmp[i-1]+tmp[i])
        ret.append(tmp[-1])
        return ret
    def generate(self, numRows: int) -> List[List[int]]:
        self.dd.clear()
        return [self.func(i) for i in range(1,numRows+1)]
# @lc code=end

