#
# @lc app=leetcode.cn id=891 lang=python3
#
# [891] 子序列宽度之和
#

# @lc code=start
from typing import List
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        ret,n,MOD=0,len(nums),1000000007
        nums.sort()
        for i in range(n):
            ret=(ret+(pow(2,i,MOD)-pow(2,n-i-1,MOD))*nums[i])%MOD
        return ret

# @lc code=end
print(Solution().sumSubseqWidths([2,1,3]))