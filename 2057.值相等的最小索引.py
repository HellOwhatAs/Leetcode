#
# @lc app=leetcode.cn id=2057 lang=python3
#
# [2057] 值相等的最小索引
#

# @lc code=start
from typing import List
class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for ii, i in enumerate(nums):
            if ii % 10 == i: return ii
        return -1
# @lc code=end

for i in [
    [0,1,2],
    [4,3,2,1],
    [1,2,3,4,5,6,7,8,9,0],
    [2,1,3,5,2]
]:
    print(Solution().smallestEqual(i))