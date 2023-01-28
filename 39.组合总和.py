#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
from typing import List
import bisect
class Solution:
    def func(self,start:int,tar:int,prev:tuple):
        if tar==0:
            self.ret.append(prev)
            return
        for i in range(start,bisect.bisect_right(self.candidates,tar)):
            self.func(i,tar-self.candidates[i],prev+(self.candidates[i],))
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates=sorted(candidates)
        self.ret=[]
        self.func(0,target,tuple())
        return list(self.ret)
# @lc code=end

