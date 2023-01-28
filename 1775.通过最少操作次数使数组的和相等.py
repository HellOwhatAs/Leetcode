#
# @lc app=leetcode.cn id=1775 lang=python3
#
# [1775] 通过最少操作次数使数组的和相等
#

# @lc code=start
from typing import List
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1,sum2=sum(nums1),sum(nums2)
        if sum1<sum2:nums1,nums2=nums2,nums1
        diff=abs(sum1-sum2)
        ret=0
        nums1.sort()
        nums2.sort()
        i1,i2=len(nums1)-1,0
        while diff>0 and (i1>=0 or i2<len(nums2)):
            if i1>=0 and i2<len(nums2):
                if nums1[i1]-1 > 6-nums2[i2]:
                    diff-=nums1[i1]-1
                    i1-=1
                else:
                    diff-=6-nums2[i2]
                    i2+=1
            elif i1>=0:
                diff-=nums1[i1]-1
                i1-=1
            else:
                diff-=6-nums2[i2]
                i2+=1
            ret+=1
        return ret if diff<=0 else -1
# @lc code=end

print(Solution().minOperations(nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]))