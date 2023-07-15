#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
from typing import List
class Solution:
    def _fourSum(self, nums: List[int], target: int):
        nums.sort()
        for a in range(len(nums) - 3):
            for b in range(a + 1, len(nums) - 2):
                c, d = b + 1, len(nums) - 1
                t = target - nums[a] - nums[b]
                while c < d:
                    if nums[c] + nums[d] == t: yield nums[a], nums[b], nums[c], nums[d]
                    if nums[c] + nums[d] < t: c += 1
                    else: d -= 1
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return [list(i) for i in set(self._fourSum(nums, target))]
# @lc code=end

print(Solution().fourSum(nums = [1,0,-1,0,-2,2], target = 0))
print(Solution().fourSum(nums = [2,2,2,2,2], target = 8))