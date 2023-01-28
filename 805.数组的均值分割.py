#
# @lc app=leetcode.cn id=805 lang=python3
#
# [805] 数组的均值分割
#

# @lc code=start
from typing import List
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n,s=len(nums),sum(nums)
        if n==1:return False
        for i in range(n):nums[i]=nums[i]*n-s
        m=n//2

        left=set()
        for i in range(1,1<<m):
            s1=sum(x for j,x in enumerate(nums[:m]) if (i>>j)&1)
            if s1==0:return True
            left.add(s1)

        for i in range(1,1<<(n-m)):
            s2=sum(x for j,x in enumerate(nums[m:]) if (i>>j)&1)
            if s2==0 or -s2 in left and i!=(1<<(n-m))-1:return True
        
        return False
# @lc code=end

print(Solution().splitArraySameAverage([1,2,3,4,5,6,7,8]))