#
# @lc app=leetcode.cn id=1470 lang=python3
#
# [1470] 重新排列数组
#

# @lc code=start
from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums[::2], nums[1::2] = nums[:n], nums[n:]
        return nums
# @lc code=end

