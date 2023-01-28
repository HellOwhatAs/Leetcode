#
# @lc app=leetcode.cn id=870 lang=python3
#
# [870] 优势洗牌
#

# @lc code=start
from typing import List
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n2=[[ind,i] for ind,i in enumerate(nums2)]
        n2.sort(key=lambda x:x[1])
        nums1.sort()
        i,ei,j=0,len(n2)-1,0
        while i<=ei and j<len(nums1):
            if nums1[j]>n2[i][1]:
                n2[i].append(nums1[j])
                i+=1
                j+=1
            else:
                n2[ei].append(nums1[j])
                ei-=1
                j+=1
        n2.sort(key=lambda x:x[0])
        return [i[2] for i in n2]
# @lc code=end

print(Solution().advantageCount(nums1 = [12,24,8,32], nums2 = [13,25,32,11]))