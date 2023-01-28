#
# @lc app=leetcode.cn id=2293 lang=python3
#
# [2293] 极大极小游戏
#

# @lc code=start
from typing import List
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nums = [max(nums[2 * i], nums[2 * i + 1]) if i%2 else  min(nums[2 * i], nums[2 * i + 1]) for i in range(len(nums)//2)]
        return nums[0]
# @lc code=end

print(Solution().minMaxGame(nums = [3]))