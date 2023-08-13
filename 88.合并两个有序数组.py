#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        t, m, n = m + n - 1, m - 1, n - 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[t] = nums1[m]
                m -= 1
            else:
                nums1[t] = nums2[n]
                n -= 1
            t -= 1
        while n >= 0:
            nums1[t] = nums2[n]
            n -= 1
            t -= 1

# @lc code=end
nums1 = [1,2,3,0,0,0]
print(Solution().merge(nums1, m = 3, nums2 = [2,5,6], n = 3))
print(nums1)

nums1 = [1]
print(Solution().merge(nums1, m = 1, nums2 = [], n = 0))
print(nums1)

nums1 = [0]
print(Solution().merge(nums1, m = 0, nums2 = [1], n = 1))
print(nums1)