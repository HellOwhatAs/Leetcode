#
# @lc app=leetcode.cn id=1630 lang=python3
#
# [1630] 等差子数组
#

# @lc code=start
from typing import List
class Solution:
    def func(self, left: int, right: int) -> bool:
        nums = [elem for elem, idx in self.nums if left <= idx < right]
        tmp = nums[1] - nums[0]
        return all(nums[i + 1] - nums[i] == tmp for i in range(1, len(nums) - 1))
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        self.nums = sorted(zip(nums, range(len(nums))))
        return [self.func(left, right + 1) for left, right in zip(l, r)]
# @lc code=end

print(Solution().checkArithmeticSubarrays(nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]))
print(Solution().checkArithmeticSubarrays(nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]))