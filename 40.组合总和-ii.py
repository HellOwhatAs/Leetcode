#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
from typing import List
import bisect
class Solution:
    dd=set()
    def func(self,start:int,tar:int,prev:tuple):
        if (tar,prev) in self.dd:return
        self.dd.add((tar,prev))
        if tar==0:
            self.ret.append(prev)
            return
        for i in range(start,bisect.bisect_right(self.candidates,tar)):
            self.func(i+1,tar-self.candidates[i],prev+(self.candidates[i],))
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates=sorted(candidates)
        self.dd.clear()
        self.ret=[]
        self.func(0,target,tuple())
        return list(self.ret)
# @lc code=end