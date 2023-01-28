#
# @lc app=leetcode.cn id=2164 lang=python3
#
# [2164] 对奇偶下标分别排序
#

# @lc code=start
from typing import List
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        return [(tmp:=(sorted(nums[::2], reverse=True), sorted(nums[1::2]))), [tmp[i%2].pop() for i in range(len(nums))]][1]
# @lc code=end

print(Solution().sortEvenOdd([4,1,2,3]))