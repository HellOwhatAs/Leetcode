#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
from typing import List
from numpy import binary_repr,int32
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret=[0]*32
        for i in nums:
            for ind,j in enumerate(binary_repr(i,width=32)):
                if j=='1':
                    ret[ind]+=1
                    ret[ind]%=3
        return int(int32(int("".join(str(i) for i in ret),2)))
# @lc code=end

