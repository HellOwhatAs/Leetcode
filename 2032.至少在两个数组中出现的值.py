#
# @lc app=leetcode.cn id=2032 lang=python3
#
# [2032] 至少在两个数组中出现的值
#

# @lc code=start
from typing import List
from collections import defaultdict
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        d=defaultdict(int)
        for s in (set(nums1),set(nums2),set(nums3)):
            for i in s:d[i]+=1
        return [k for k,v in d.items() if v>=2]
# @lc code=end

