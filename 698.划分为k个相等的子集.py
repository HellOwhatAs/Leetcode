#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#

# @lc code=start
from typing import List, Tuple
from itertools import combinations
def mycache(dd):
    def _mycache(func):
        def ret(self,x):
            if x in dd:return dd[x]
            tmp=func(self,x)
            dd[x]=tmp
            return tmp
        return ret
    return _mycache
class Solution:
    dd={}
    def subsets(self, nums: Tuple[int]) -> List[Tuple[int]]:
        return [j for i in range(len(nums)) for j in combinations(nums,i)]
    def Tuplesub(self,a:Tuple[int],b:Tuple[int])->Tuple[int]:
        ret=list(a)
        for i in b:ret.remove(i)
        return tuple(ret)
    @mycache(dd)
    def func(self,nums: Tuple[int]):
        if not nums:return True
        if sum(nums)==self.val:return True
        for i in self.subsets(nums):
            if sum(i)==self.val:
                if self.func(self.Tuplesub(nums,i)):
                    return True
        return False
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total=sum(nums)
        if total%k:return False
        self.val=total//k
        nums.sort(reverse=True)
        if nums[0]>self.val:return False
        self.dd.clear()
        return self.func(tuple(nums))

# @lc code=end