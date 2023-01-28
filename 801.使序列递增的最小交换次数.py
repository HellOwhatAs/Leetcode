#
# @lc app=leetcode.cn id=801 lang=python3
#
# [801] 使序列递增的最小交换次数
#

# @lc code=start
from typing import List
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        d0,d1=0,1
        for i in range(1,len(nums1)):
            a,b=nums1[i]>nums1[i-1] and nums2[i]>nums2[i-1], nums1[i]>nums2[i-1] and nums2[i]>nums1[i-1]
            if a and b:
                d0,d1=min(d0,d1),min(d0,d1)+1
            elif a:
                d1+=1
            elif b:
                d0,d1=d1,d0+1
        return min(d0,d1)
# @lc code=end

print(Solution().minSwap(nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]))